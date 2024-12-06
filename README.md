# RabbitMQ Messaging Service - Study Project

This is a study project to explore RabbitMQ messaging. The idea is to simulate message sending from a service (like Amazon) to a supplier using RabbitMQ for communication.

## Purpose

The goal is to learn and test RabbitMQ for messaging between systems. The project simulates scenarios like:

- **Example 1**: Amazon sends a message to the supplier about a product purchase.
- **Example 2**: A microservices system, like Uber, processes millions of messages using RabbitMQ for real-time event handling.

## Technologies and Dependencies

This project uses the following dependencies:

- **`pika==1.3.2`**: Python library to communicate with RabbitMQ.
- **`python-dotenv==1.0.1`**: To load environment variables from a `.env` file.
- 
