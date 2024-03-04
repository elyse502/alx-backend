import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', function () {
    console.log('Redis client connected to the server');
});

redisClient.on('error', function (error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

// Subscribe to Holberton school channel.
redisClient.subscribe('holberton school channel');

// Listen for messages on channel and print message when received.
redisClient.on('message', function (channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
// Unsubscribe from channel and cancel server connection.
    redisClient.unsubscribe('holberton school channel');
    redisClient.end(true);
  }
});
