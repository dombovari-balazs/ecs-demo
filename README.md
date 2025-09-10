# ecs-demo
In this repo I would like to demo how to create an ecs task with terraform, display  something received from dynamodb on a publicly available API.


## Best practices
Following best practices from here:

https://github.com/zhanymkanov/fastapi-best-practices


## How to test
Not sure how to resolve path issue, this seems like a good fix. 
Supports:
- running from terminal
``` sh 
python -m pytest tests
```

- running from VS Code test runner


(by default, running only "pytest" should work.)


## Guides

Terraform setup

https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli


Terraform with ECS Fargate 

https://github.com/terraform-aws-modules/terraform-aws-ecs/tree/master/examples/fargate


Docker in docker? 

https://www.reddit.com/r/docker/comments/1ahizyj/devcontainers_docker_in_docker_or_docker_outside/



Connect Github Actions to AWS

--> seems like OpenID connector is the GoTo solution

https://medium.com/@alissonpdc/github-actions-how-to-authenticate-on-aws-cloud-14185f811bf0
https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/
https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws


Connect ECS with other services
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-connecting-vpc.html
---> seems like a VPC challange


az kom gec
https://github.com/actions/starter-workflows/blob/main/deployments/aws.yml
https://github.com/actions/starter-workflows/blob/main/deployments/terraform.yml


## Questions
- Do we want to be able to directly push images to ECR from our local machine?
In the first run, let's just focus on solving 1 problem at once. Later this option could add value and reduce development cycle.
Also helps quick fixes, however adds security risks as well.

