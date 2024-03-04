# 0x03. Queuing System in JS

![1486e02a78cdf7b4557c](https://github.com/elyse502/alx-backend/assets/125453474/a808c0eb-7651-4107-b1f3-6d8e5c7cc056)

# Resources🏗️
<b>Read or watch:</b>
* [Redis quick start](https://redis.io/docs/install/install-redis/)
* [Redis client interface](https://redis.io/docs/connect/cli/)
* [Redis client for Node JS](https://github.com/redis/node-redis)
* [Kue](https://github.com/Automattic/kue) _deprecated but still use in the industry_

# Learning Objectives 📖
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:
* How to run a Redis server on your machine
* How to run simple operations with the Redis client
* How to use a Redis client with Node JS for basic operations
* How to store hash values in Redis
* How to deal with async operations with Redis
* How to use Kue as a queue system
* How to build a basic Express app interacting with a Redis server
* How to the build a basic Express app interacting with a Redis server and queue

# Requirements 🏛️
* All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
* All of your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `js` extension

# Required Files for the Project 🗃️
**`package.json`**
<details>
  <summary>Click to show/hide file contents</summary>
  
```groovy

{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }

```
</details>


**`.babelrc`**
<details>
  <summary>Click to show/hide file contents</summary>
  
```groovy

{
  "presets": [
    "@babel/preset-env"
  ]
}

```
</details>


**and…**

Don’t forget to run `$ npm install` when you have the `package.json`


# Tasks 📃
## 0. Install a redis instance: [README.md](README.md), [dump.rdb](dump.rdb)
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/download/](https://redis.io/download/)):

```groovy
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```

* Start Redis in the background with `src/redis-server`
```groovy
$ src/redis-server &
```
* Make sure that the server is working with a ping `src/redis-cli ping`
> PONG

* Using the Redis client again, set the value `School` for the key `Holberton`
```groovy
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

* Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)
```groovy
$ kill [PID_OF_Redis_Server]
```
Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

### Requirements:

* Running `get Holberton` in the client, should return `School`



































































