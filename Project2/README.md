# Hurricave Harvey Damage Classification Report
## Overview
In this project, we develop various neural networks thata are trained on a dataset of satellite images from Texas after Hurricane Harvey, such that they can predict whether or not a building is damaged. We explore how we prepare the data, design and train the models, evaluate the models, and deploy our inference server, so users can interact with the model.  

## Deploying the Inference Server
For simplification, we use a Makefile to automate the building and deployment of the Docker container that contains our best neural network model. If the user uses the Makefile, by default it will bring any existing container down and then restart it:  
```make```  

If the user wishes to rebuild the image (e.g., if they modified Dockerfile or requirements.txt which directly impacts the build), they can run:  
```make build```  

Finally, if the user wants to guarantee a completely fresh build, they can run the following command, although this will take significantly more time than the previous approaches:  
```make clean```

Doing any of the above 3 commands will start the container on the local machine and expose port 5000. This allows the user to interact with the inference server over the network using a REST API.

## Making Requests
The user can make 2 types of requests to interact with our inference server.  

### 1. `/summary` (GET)
If the user would like a summary of the model's metadata, they can send a GET request to /summary:  
```curl localhost:5000/summary```
Here is an example:  
```
ubuntu@tavishka-vm:~$ curl localhost:5000/summary
{
  "author": "Tav",
  "framework": "TensorFlow/Keras",
  "image_size": [
    64,
    64
  ],
  "input_shape": [
    null,
    64,
    64,
    3
  ],
  "model_name": "best_model.keras",
  "output_shape": [
    null,
    1
  ],
  "parameters": 2030145
}
```

### 2. `/inference` (POST)
If the user would like to post an image of a house, so the model can predict whether or not it is damaged, they can send a multipart POST request to /inference:  
```curl -X POST -F "image=@<path_to_house_img>" localhost:5000/inference```

Here is an example:  
```
ubuntu@luke-venk-vm:~/coe379l-fa25/code/Project2/data/damage$ curl -X POST -F "image=@-93.66109_30.212114.jpeg" localhost:5000/inference
{
  "prediction": "damage"
}
```

#### Running the Grader
To automate testing the performance of our model, a grader has been created to automatically make several requests to our inference server and determine its accuracy. The directory for the grader can be found at the following link:  
https://github.com/joestubbs/coe379l-fa25/tree/main/code/Project2

To run the grader locally, first clone the repository, and navigate to `coe379l-fa25/code/Project2`. In a separate shell, follow the instructions above to deploy the inference server. Finally, as the instructions in the grader state, run the following command in the first shell:  
```./start_grader.sh```  

If the model performs as expected, the output should look like the following:  
TODO: update
```
**** STARTING GRADING ****

ERROR: GET /summary is INVALID. Non-200 status code; Status code received: 418
Starting full POST test suite...
POST /inference format correct for input /data/damage/-93.66109_30.212114.jpeg AND prediction was correct!
POST /inference format correct for input /data/damage/-93.79252_30.039519.jpeg AND prediction was correct!
POST /inference format correct for input /data/damage/-93.73643_29.788717.jpeg AND prediction was correct!
POST /inference format correct for input /data/no_damage/-95.06212_29.829257000000002.jpeg AND prediction was correct!
POST /inference format correct for input /data/no_damage/-95.6302_29.768889.jpeg AND prediction was correct!
POST /inference format correct for input /data/no_damage/-95.6567_29.835759999999997.jpeg AND prediction was correct!
Final results:
Total correct: 6
Total Inferences: 6
Accuracy: 1.0
```
