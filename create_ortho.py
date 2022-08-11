import os
import time
import subprocess
from pyodm import Node, exceptions

import sys
sys.path.append('..')

# subprocess.run(['gsutil', '-m', 'cp', '-r', f'gs://drone-images/example', './data'])

node = Node("localhost", 3000)

# images = os.listdir('data/2018-11-14_avdelning_Ribbfors_1-3')
# images = [os.path.join('data/2018-11-14_avdelning_Ribbfors_1-3', im) for im in images]
# images = os.listdir('data/small_test')
# images = [os.path.join('data/small_test', im) for im in images]
images = os.listdir('data/example')
images = [os.path.join('data/example', im) for im in images]
print(images)

try:
    # Start a task
    print("Uploading images...")
    task = node.create_task(images, {
        'dsm': True, 
        'orthophoto-resolution': 0.2,
        'dem-resolution': 2.,
        'feature-quality': 'high',
        'pc-quality': 'high',
        'orthophoto-kmz': True
        })
    print(task.info())

    try:
        # This will block until the task is finished
        # or will raise an exception
        start = time.time()
        task.wait_for_completion()
        end = time.time()
        print('Execution time: ', end - start)

        print("Task completed, downloading results...")

        # Retrieve results
        task.download_assets("./results")

        print("Assets saved in ./results (%s)" % os.listdir("./results"))

        # subprocess.run(['gsutil', '-m', 'cp', '-r', './result/' f'gs://drone-images/example'])

        # Restart task and this time compute dtm
        task.restart({'dtm': True})
        task.wait_for_completion()

        print("Task completed, downloading results...")

        task.download_assets("./results_with_dtm")

        print("Assets saved in ./results_with_dtm (%s)" % os.listdir("./results_with_dtm"))
    except exceptions.TaskFailedError as e:
        print("\n".join(task.output()))

except exceptions.NodeConnectionError as e:
    print("Cannot connect: %s" % e)
except exceptions.NodeResponseError as e:
    print("Error: %s" % e)
