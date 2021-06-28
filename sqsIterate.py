# simple functions to help find the queue we care about

# looks up queues available, passes to iterateTags to see whether this is the one we want
def iterateQueues(client, tagName, tagValue):
    # find the queue URL by tag
    queueResponse = client.list_queues()

    # loop through the queues
    for queue in queueResponse['QueueUrls']:
        # query the queue for its tags
        if iterateTags(client, queue, tagName, tagValue):
            return queue
        else:
            return False

# looks up tags associated with the queue.  Returns True/False depending if found
def iterateTags(client, queue, tagName, tagValue):
    tagResponse = client.list_queue_tags(
        QueueUrl = queue
    )

    if 'Project' in tagResponse['Tags']:
        if tagResponse['Tags'][tagName] == tagValue:
            # found it, stop looking
            return True

    # sad trombone sound
    return False
