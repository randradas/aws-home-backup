import aws_cdk as core
import aws_cdk.assertions as assertions

from backup_storage.backup_storage_stack import BackupStorageStack

# example tests. To run these tests, uncomment this file along with the example
# resource in backup_storage/backup_storage_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BackupStorageStack(app, "backup-storage")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
