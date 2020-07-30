# A data scientist's guide to deploying machine learning models

![](https://img.shields.io/badge/-tutorial-informational)
![](https://img.shields.io/badge/-machine--learning-important)
![](https://img.shields.io/badge/-aws-lightgrey)

<img align="right" src="docs/img/ml-deploy.png" width="250">

The aim of this repository is to provide a simple guide to deploying machine learning (ML) models for data scientists familiar with machine learning in a local environment, but interested in learning how to deploy their models. Deployment refers to the act of making your ML model available in a production environment, where it can be accessed and utilised by other software.

Perhaps surprisingly, deployment is a process that is quite unfamiliar to many data scientists - in large part due to the need for some level of familiarity with software engineering. Fortunately, there are many tools available to help us data scientists with deploying our models. This repository focuses on currently and 

### My recommendations for deploying ML models

Having gone through the process of deploying a ML model via different methods/tools, I have a slight preference for Amazon SageMaker. Not only is it highly scalable, but, in addition, everything related to your model/service can be kept in one place: data in S3, notebooks in SageMaker, APIs in API Gateway, etc. However, in saying that, Flask has its use cases too, not only does it provide an easy method of developing a web application (not just an endpoint), but it is free and I found it slightly easier to learn than SageMaker. As always with ML, there's no free lunch and the right tool for the job depends on the job itself.
