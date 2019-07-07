# pythockerserv

* [Install serverless](https://serverless.com/framework/docs/providers/aws/guide/quick-start/)
* [Create AWS credentials](https://serverless.com/framework/docs/providers/aws/guide/credentials#creating-aws-access-keys)
* Store the access and secret key in `~/.aws/credentials` for example under `sls-dev` AWS profile.

    ```bash
    [sls-dev]
    aws_access_key_id = AKIAVEQZS4EXLWYOUG5H
    aws_secret_access_key = XmUuaQY5RXzTn71eXZx6uz1IF32MPDn7ptD/1RDH
    ```

* Set the AWS profile in your bash environment

    ```bash
    export AWS_PROFILE=sls-dev
    ```

* Deploy

  ```bash
  serverless deploy -v
  ```

* Invoke the function

  ```bash
  serverless invoke -f pythockerize -v
  {
      "statusCode": 200,
      "body": [
          "linesample"
      ]
  }
  ```

## Links

* https://serverless.com/framework/docs/providers/aws/examples/hello-world/python/
* https://serverless.com/framework/docs/providers/aws/guide/deploying/
* https://serverless.com/blog/serverless-python-packaging/
* https://serverless.com/blog/serverless-secrets-api-keys/
* https://hackernoon.com/you-should-use-ssm-parameter-store-over-lambda-env-variables-5197fc6ea45b

* https://github.com/UnitedIncome/serverless-python-requirements
* https://pypi.org/project/pypi-simple/
* https://pygithub.readthedocs.io/en/latest/github.html
