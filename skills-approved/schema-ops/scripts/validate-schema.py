#!/usr/bin/env python3
"""
Schema Ops — JSON-LD Structured Data Validator

Validates JSON-LD schema markup for common errors, missing required properties,
and rich result eligibility. Designed for affiliate marketing sites.

Usage:
    python3 validate-schema.py schema.json
    python3 validate-schema.py --inline '{"@context":"https://schema.org","@type":"Product",...}'
    cat schema.json | python3 validate-schema.py -

Requirements: Python 3.6+ (standard library only)
"""

import json
import sys
import re
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

# ---------------------------------------------------------------------------
# Schema type definitions: required + recommended properties per @type
# ---------------------------------------------------------------------------
SCHEMA_REQUIREMENTS = {
    "Product": {
        "required": ["name"],
        "recommended": ["image", "description", "brand", "sku", "gtin13", "mpn",
                         "aggregateRating", "review", "offers"],
        "rich_result_required": {
            "stars": ["aggregateRating"],
            "price": ["offers"],
        }
    },
    "Review": {
        "required": ["reviewRating", "author"],
        "recommended": ["itemReviewed", "datePublished", "reviewBody", "publisher",
                         "headline"],
    },
    "AggregateRating": {
        "required": ["ratingValue", "reviewCount"],
        "recommended": ["bestRating", "worstRating", "ratingCount"],
    },
    "Rating": {
        "required": ["ratingValue"],
        "recommended": ["bestRating", "worstRating"],
    },
    "Offer": {
        "required": ["price", "priceCurrency"],
        "recommended": ["availability", "url", "priceValidUntil", "itemCondition",
                         "seller"],
    },
    "AggregateOffer": {
        "required": ["lowPrice", "priceCurrency"],
        "recommended": ["highPrice", "offerCount", "offers"],
    },
    "Article": {
        "required": ["headline", "datePublished", "author"],
        "recommended": ["image", "dateModified", "publisher", "description",
                         "mainEntityOfPage", "wordCount", "articleSection"],
    },
    "BlogPosting": {
        "required": ["headline", "datePublished", "author"],
        "recommended": ["image", "dateModified", "publisher", "description"],
    },
    "FAQPage": {
        "required": ["mainEntity"],
        "recommended": [],
    },
    "Question": {
        "required": ["name", "acceptedAnswer"],
        "recommended": [],
    },
    "Answer": {
        "required": ["text"],
        "recommended": [],
    },
    "HowTo": {
        "required": ["name", "step"],
        "recommended": ["description", "totalTime", "tool", "supply", "image"],
    },
    "HowToStep": {
        "required": ["text"],
        "recommended": ["name", "image", "url"],
    },
    "ItemList": {
        "required": ["itemListElement"],
        "recommended": ["name", "description", "numberOfItems"],
    },
    "ListItem": {
        "required": ["position", "item"],
        "recommended": ["name", "url"],
    },
    "BreadcrumbList": {
        "required": ["itemListElement"],
        "recommended": [],
    },
    "Organization": {
        "required": ["name", "url"],
        "recommended": ["logo", "sameAs", "description", "contactPoint",
                         "foundingDate", "founder"],
    },
    "Person": {
        "required": ["name"],
        "recommended": ["url", "image", "jobTitle", "description", "sameAs",
                         "worksFor", "knowsAbout"],
    },
    "SoftwareApplication": {
        "required": ["name", "applicationCategory"],
        "recommended": ["operatingSystem", "offers", "aggregateRating", "description",
                         "screenshot", "featureList", "softwareVersion", "url"],
    },
    "WebSite": {
        "required": ["name", "url"],
        "recommended": ["potentialAction", "publisher", "description"],
    },
    "VideoObject": {
        "required": ["name", "description", "thumbnailUrl", "uploadDate"],
        "recommended": ["duration", "contentUrl", "embedUrl", "interactionStatistic"],
    },
    "Brand": {
        "required": ["name"],
        "recommended": ["url", "logo"],
    },
    "ImageObject": {
        "required": ["url"],
        "recommended": ["width", "height", "caption"],
    },
}

# ---------------------------------------------------------------------------
# Validation result classes
# ---------------------------------------------------------------------------
class ValidationError:
    def __init__(self, path: str, message: str, severity: str = "error"):
        self.path = path
        self.message = message
        self.severity = severity  # "error", "warning", "info"

    def __str__(self):
        icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}[self.severity]
        return f"{icon} [{self.severity.upper()}] {self.path}: {self.message}"


class ValidationResult:
    def __init__(self):
        self.errors: List[ValidationError] = []

    def add_error(self, path: str, msg: str):
        self.errors.append(ValidationError(path, msg, "error"))

    def add_warning(self, path: str, msg: str):
        self.errors.append(ValidationError(path, msg, "warning"))

    def add_info(self, path: str, msg: str):
        self.errors.append(ValidationError(path, msg, "info"))

    @property
    def has_errors(self) -> bool:
        return any(e.severity == "error" for e in self.errors)

    @property
    def has_warnings(self) -> bool:
        return any(e.severity == "warning" for e in self.errors)

    def summary(self) -> str:
        errs = sum(1 for e in self.errors if e.severity == "error")
        warns = sum(1 for e in self.errors if e.severity == "warning")
        infos = sum(1 for e in self.errors if e.severity == "info")
        parts = []
        if errs: parts.append(f"{errs} error(s)")
        if warns: parts.append(f"{warns} warning(s)")
        if infos: parts.append(f"{infos} info(s)")
        return ", ".join(parts) if parts else "All checks passed ✅"


# ---------------------------------------------------------------------------
# Individual validators
# ---------------------------------------------------------------------------
def validate_url(value: str, path: str, result: ValidationResult):
    if not isinstance(value, str):
        result.add_error(path, f"Expected string URL, got {type(value).__name__}")
        return
    if not value.startswith(("http://", "https://")):
        result.add_error(path, f"URL must be absolute (start with http:// or https://): '{value[:60]}'")
    if value.startswith("http://"):
        result.add_warning(path, "URL uses http:// — prefer https:// for security and SEO")


def validate_date(value: str, path: str, result: ValidationResult):
    if not isinstance(value, str):
        result.add_error(path, f"Expected string date, got {type(value).__name__}")
        return
    # ISO 8601 patterns
    iso_patterns = [
        r"^\d{4}-\d{2}-\d{2}$",                          # 2026-03-12
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$",       # 2026-03-12T00:00:00
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$",      # 2026-03-12T00:00:00Z
        r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$",  # with timezone
    ]
    if not any(re.match(p, value) for p in iso_patterns):
        result.add_warning(path, f"Date '{value}' doesn't match ISO 8601 format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ)")


def validate_duration(value: str, path: str, result: ValidationResult):
    if not isinstance(value, str):
        result.add_error(path, f"Expected string duration, got {type(value).__name__}")
        return
    # ISO 8601 duration: PT1H30M, PT20M, PT15M32S
    if not re.match(r"^P(\d+Y)?(\d+M)?(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?)?$", value):
        result.add_warning(path, f"Duration '{value}' doesn't match ISO 8601 duration format (e.g., PT1H30M, PT20M)")


def validate_rating_value(value: Any, path: str, result: ValidationResult):
    if value is None:
        return
    if not isinstance(value, str):
        result.add_error(path, f"Rating value should be a string, got {type(value).__name__}: {value}")
        return
    try:
        num = float(value)
        if num < 0 or num > 5:
            result.add_warning(path, f"Rating value {num} is outside typical 0-5 range")
    except ValueError:
        result.add_error(path, f"Rating value '{value}' is not a valid number")


def validate_price(value: Any, path: str, result: ValidationResult):
    if value is None:
        return
    if not isinstance(value, str):
        result.add_warning(path, f"Price should be a string, got {type(value).__name__}: {value}")
        return
    try:
        float(value)
    except ValueError:
        result.add_error(path, f"Price '{value}' is not a valid number")


def validate_image_url(value: Any, path: str, result: ValidationResult):
    if isinstance(value, str):
        validate_url(value, path, result)
        if not any(value.lower().endswith(ext) for ext in
                   ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp']):
            result.add_warning(path, f"Image URL doesn't have a common image extension: '{value[:60]}'")
    elif isinstance(value, dict):
        if "@type" in value and value["@type"] == "ImageObject":
            if "url" not in value:
                result.add_error(path, "ImageObject missing required 'url' property")
            else:
                validate_url(value["url"], f"{path}.url", result)
        else:
            validate_url(value.get("url", ""), path, result)
    elif isinstance(value, list):
        for i, img in enumerate(value):
            validate_image_url(img, f"{path}[{i}]", result)


def validate_same_as(value: Any, path: str, result: ValidationResult):
    if isinstance(value, list):
        for i, url in enumerate(value):
            validate_url(url, f"{path}[{i}]", result)
    elif isinstance(value, str):
        validate_url(value, path, result)


def validate_availability(value: Any, path: str, result: ValidationResult):
    if not isinstance(value, str):
        return
    valid_urls = [
        "https://schema.org/InStock",
        "https://schema.org/OutOfStock",
        "https://schema.org/PreOrder",
        "https://schema.org/BackOrder",
        "https://schema.org/SoldOut",
        "https://schema.org/Discontinued",
        "https://schema.org/InStoreOnly",
        "https://schema.org/OnlineOnly",
        "https://schema.org/LimitedAvailability",
    ]
    if value not in valid_urls:
        result.add_warning(path, f"Unusual availability value: '{value}'. Expected one of: InStock, OutOfStock, PreOrder, etc.")


# ---------------------------------------------------------------------------
# Recursive schema node validator
# ---------------------------------------------------------------------------
def validate_node(node: Any, path: str, result: ValidationResult):
    """Recursively validate a schema.org JSON-LD node."""
    if node is None:
        return

    if isinstance(node, list):
        for i, item in enumerate(node):
            validate_node(item, f"{path}[{i}]", result)
        return

    if not isinstance(node, dict):
        return

    # Check @context
    if path == "$" or path == "$.graph[?]":
        ctx = node.get("@context")
        if ctx and ctx != "https://schema.org":
            result.add_warning(f"{path}.__context",
                               f"@context is '{ctx}' — expected 'https://schema.org'")

    schema_type = node.get("@type")
    if not schema_type:
        result.add_warning(path, "Node missing @type")
        return

    # Handle @type as list (multiple types)
    if isinstance(schema_type, list):
        for t in schema_type:
            validate_type_properties(node, t, path, result)
    else:
        validate_type_properties(node, schema_type, path, result)

    # Recurse into known sub-objects
    for key, value in node.items():
        if key.startswith("@"):
            continue
        child_path = f"{path}.{key}"
        if isinstance(value, dict):
            validate_node(value, child_path, result)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    validate_node(item, f"{child_path}[{i}]", result)


def validate_type_properties(node: dict, schema_type: str, path: str, result: ValidationResult):
    """Validate required/recommended properties for a specific @type."""
    type_key = schema_type
    if type_key not in SCHEMA_REQUIREMENTS:
        result.add_info(path, f"Unknown @type '{schema_type}' — no validation rules defined")
        return

    reqs = SCHEMA_REQUIREMENTS[type_key]

    # Check required properties
    for prop in reqs["required"]:
        if prop not in node:
            result.add_error(f"{path}.{prop}",
                             f"'{schema_type}' requires property '{prop}'")

    # Check recommended properties
    for prop in reqs["recommended"]:
        if prop not in node:
            result.add_warning(f"{path}.{prop}",
                               f"'{schema_type}' should have property '{prop}' (recommended)")

    # Type-specific validation
    _validate_specific_fields(node, schema_type, path, result)


def _validate_specific_fields(node: dict, schema_type: str, path: str, result: ValidationResult):
    """Run field-level validators based on known property semantics."""

    # URLs
    for url_prop in ["url", "item", "contentUrl", "embedUrl", "thumbnailUrl"]:
        if url_prop in node:
            val = node[url_prop]
            if isinstance(val, str):
                validate_url(val, f"{path}.{url_prop}", result)
            elif isinstance(val, dict) and "url" in val:
                validate_url(val["url"], f"{path}.{url_prop}.url", result)

    # @id
    if "@id" in node:
        id_val = node["@id"]
        if isinstance(id_val, str) and not id_val.startswith("#"):
            validate_url(id_val, f"{path}.__id", result)

    # Images
    for img_prop in ["image", "logo", "screenshot", "thumbnailUrl"]:
        if img_prop in node:
            validate_image_url(node[img_prop], f"{path}.{img_prop}", result)

    # Dates
    for date_prop in ["datePublished", "dateModified", "priceValidUntil",
                       "foundingDate", "uploadDate", "expires"]:
        if date_prop in node and isinstance(node[date_prop], str):
            validate_date(node[date_prop], f"{path}.{date_prop}", result)

    # Durations
    for dur_prop in ["totalTime", "duration"]:
        if dur_prop in node and isinstance(node[dur_prop], str):
            validate_duration(node[dur_prop], f"{path}.{dur_prop}", result)

    # Ratings
    for rating_container in ["aggregateRating", "reviewRating"]:
        if rating_container in node and isinstance(node[rating_container], dict):
            rating_node = node[rating_container]
            if "ratingValue" in rating_node:
                validate_rating_value(rating_node["ratingValue"],
                                      f"{path}.{rating_container}.ratingValue", result)
            if "bestRating" in rating_node:
                validate_rating_value(rating_node["bestRating"],
                                      f"{path}.{rating_container}.bestRating", result)

    # Prices
    for price_prop in ["price", "lowPrice", "highPrice"]:
        if price_prop in node:
            validate_price(node[price_prop], f"{path}.{price_prop}", result)

    # Offer availability
    if "availability" in node and schema_type in ("Offer", "AggregateOffer"):
        validate_availability(node["availability"], f"{path}.availability", result)

    # SameAs
    if "sameAs" in node:
        validate_same_as(node["sameAs"], f"{path}.sameAs", result)

    # ItemList checks
    if schema_type == "ItemList":
        items = node.get("itemListElement", [])
        if isinstance(items, list) and len(items) == 0:
            result.add_warning(f"{path}.itemListElement", "ItemList has empty itemListElement")
        declared_count = node.get("numberOfItems")
        if declared_count and isinstance(items, list):
            try:
                if int(declared_count) != len(items):
                    result.add_warning(f"{path}.numberOfItems",
                                       f"numberOfItems ({declared_count}) doesn't match itemListElement count ({len(items)})")
            except (ValueError, TypeError):
                pass
        # Check positions are sequential
        if isinstance(items, list) and items:
            positions = []
            for i, item in enumerate(items):
                if isinstance(item, dict) and "position" in item:
                    try:
                        positions.append((i, int(item["position"])))
                    except (ValueError, TypeError):
                        pass
            if positions:
                expected = list(range(1, len(positions) + 1))
                actual = [p[1] for p in positions]
                if actual != expected:
                    result.add_warning(f"{path}.itemListElement",
                                       f"ListItem positions not sequential: {actual} (expected {expected})")

    # BreadcrumbList checks
    if schema_type == "BreadcrumbList":
        items = node.get("itemListElement", [])
        if isinstance(items, list):
            for i, item in enumerate(items):
                if isinstance(item, dict):
                    if item.get("@type") == "ListItem" and "position" not in item:
                        result.add_error(f"{path}.itemListElement[{i}].position",
                                         "BreadcrumbList ListItem missing 'position'")
                    if item.get("@type") == "ListItem" and "name" not in item:
                        result.add_error(f"{path}.itemListElement[{i}].name",
                                         "BreadcrumbList ListItem missing 'name'")

    # FAQPage checks
    if schema_type == "FAQPage":
        entities = node.get("mainEntity", [])
        if isinstance(entities, list):
            if len(entities) < 2:
                result.add_warning(f"{path}.mainEntity",
                                   f"FAQPage has only {len(entities)} question(s) — minimum 2 recommended for rich results")
            for i, q in enumerate(entities):
                if isinstance(q, dict):
                    if q.get("@type") == "Question":
                        if "name" not in q:
                            result.add_error(f"{path}.mainEntity[{i}].name",
                                             "Question missing 'name'")
                        if "acceptedAnswer" not in q:
                            result.add_error(f"{path}.mainEntity[{i}].acceptedAnswer",
                                             "Question missing 'acceptedAnswer'")
                        elif isinstance(q["acceptedAnswer"], dict):
                            if "text" not in q["acceptedAnswer"]:
                                result.add_error(f"{path}.mainEntity[{i}].acceptedAnswer.text",
                                                 "Answer missing 'text'")

    # HowTo checks
    if schema_type == "HowTo":
        steps = node.get("step", [])
        if isinstance(steps, list):
            if len(steps) < 2:
                result.add_warning(f"{path}.step",
                                   f"HowTo has only {len(steps)} step(s) — minimum 2 required for rich results")
            has_images = False
            for i, step in enumerate(steps):
                if isinstance(step, dict):
                    if "text" not in step and "itemListElement" not in step:
                        result.add_error(f"{path}.step[{i}]",
                                         "HowToStep missing 'text' (or 'itemListElement')")
                    if "image" in step:
                        has_images = True
            if not has_images:
                result.add_info(f"{path}.step",
                                "No step images found — adding images improves How-To rich result appearance")

    # Product star rating check
    if schema_type == "Product":
        has_aggregate = "aggregateRating" in node
        has_review = "review" in node
        if not has_aggregate and not has_review:
            result.add_info(f"{path}",
                            "Product has no aggregateRating or review — no star ratings will appear in SERPs")


# ---------------------------------------------------------------------------
# Entry point: parse and validate
# ---------------------------------------------------------------------------
def validate_schema(data: Any) -> ValidationResult:
    result = ValidationResult()

    # Handle @graph
    if isinstance(data, dict):
        if "@graph" in data:
            graph = data["@graph"]
            if isinstance(graph, list):
                for i, node in enumerate(graph):
                    validate_node(node, f"$.graph[{i}]", result)
            else:
                result.add_error("$.graph", "@graph should be an array")
            # Validate top-level context
            ctx = data.get("@context")
            if ctx and ctx != "https://schema.org":
                result.add_warning("$.__context",
                                   f"@context is '{ctx}' — expected 'https://schema.org'")
        else:
            validate_node(data, "$", result)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            validate_node(item, f"$[{i}]", result)
    else:
        result.add_error("$", f"Expected JSON object or array, got {type(data).__name__}")

    return result


def load_from_file(filepath: str) -> Any:
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def print_results(result: ValidationResult, source: str):
    print(f"\n{'='*60}")
    print(f"Schema Validation Report: {source}")
    print(f"{'='*60}\n")

    if not result.errors:
        print("✅ All checks passed! Schema looks good.\n")
        return

    # Group by severity
    errors = [e for e in result.errors if e.severity == "error"]
    warnings = [e for e in result.errors if e.severity == "warning"]
    infos = [e for e in result.errors if e.severity == "info"]

    if errors:
        print(f"❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"   {e}")
        print()

    if warnings:
        print(f"⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"   {w}")
        print()

    if infos:
        print(f"ℹ️  INFO ({len(infos)}):")
        for i in infos:
            print(f"   {i}")
        print()

    print(f"Summary: {result.summary()}\n")

    if errors:
        print("🔴 Fix all errors before deploying. Errors prevent rich results.")
    elif warnings:
        print("🟡 No errors, but fix warnings for best rich result eligibility.")
    else:
        print("🟢 Schema is valid with only informational notes.")
    print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "-":
        # Read from stdin
        try:
            data = json.load(sys.stdin)
            source = "stdin"
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON from stdin: {e}")
            sys.exit(1)
    elif arg == "--inline":
        # Inline JSON passed as second argument
        if len(sys.argv) < 3:
            print("❌ --inline requires a JSON string argument")
            sys.exit(1)
        try:
            data = json.loads(sys.argv[2])
            source = "inline"
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            sys.exit(1)
    elif arg.startswith("{") or arg.startswith("["):
        # Inline JSON (bare, no flag)
        try:
            data = json.loads(arg)
            source = "inline"
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            sys.exit(1)
    else:
        # File path
        try:
            data = load_from_file(arg)
            source = arg
        except FileNotFoundError:
            print(f"❌ File not found: {arg}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in {arg}: {e}")
            sys.exit(1)

    result = validate_schema(data)
    print_results(result, source)

    sys.exit(1 if result.has_errors else 0)


if __name__ == "__main__":
    main()
