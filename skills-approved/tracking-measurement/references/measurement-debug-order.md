# Measurement Debug Order

Check in this order:
1. what business event actually matters
2. what should fire on that event
3. whether the event fires at all
4. whether required parameters are present
5. whether deduplication works
6. whether the destination receives and classifies it correctly
7. whether reporting aligns across systems within an acceptable gap

## High-risk fields
- transaction_id
- event_id
- value
- currency
- lead qualification metadata
- source / medium / campaign context
