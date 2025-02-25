# M-Pesa Express Integration

This repository provides a Node.js library designed to facilitate seamless integration with Safaricom's M-Pesa Express (Lipa Na M-Pesa Online) API. It enables businesses and developers to initiate M-Pesa payment requests directly from their applications, enhancing the payment experience for users.

## Features

- **STK Push Integration**: Initiate payment requests that prompt users to authorize payments on their M-Pesa registered devices.
- **Transaction Status Query**: Check the status of initiated payment requests to confirm their outcomes.
- **C2B (Customer to Business) Simulation**: Simulate payment transactions from customers to businesses for testing purposes.
- **B2C (Business to Customer) Payments**: Disburse funds from businesses to customers directly through M-Pesa.

## Prerequisites

- **Node.js**: Ensure you have Node.js installed.
- **Safaricom Developer Account**: Register at the [Safaricom Developer Portal](https://developer.safaricom.co.ke/) to obtain API credentials.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/pascalspencer/M-pesa-Express.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd M-pesa-Express
   ```

3. **Install Dependencies**:

   ```bash
   npm install
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the root directory and add the following:

   ```env
   CONSUMER_KEY=your_consumer_key
   CONSUMER_SECRET=your_consumer_secret
   SHORTCODE=your_shortcode
   PASSKEY=your_lipa_na_mpesa_online_passkey
   CALLBACK_URL=your_callback_url
   ```

   Replace placeholders with your actual credentials and URLs.

## Usage

The library provides functions to interact with various M-Pesa services. Below is an example of initiating an STK Push payment request:

```javascript
const mpesa = require('./mpesa'); // Adjust the path as necessary

const paymentData = {
  amount: 100,
  phoneNumber: '2547XXXXXXXX',
  accountReference: 'REF123',
  transactionDescription: 'Payment for services',
};

mpesa
  .lipaNaMpesaOnline(paymentData)
  .then((response) => {
    console.log('Payment initiated successfully:', response);
  })
  .catch((error) => {
    console.error('Error initiating payment:', error);
  });
```


Ensure you replace `'2547XXXXXXXX'` with the customer's phone number and adjust other parameters as needed.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.


## Acknowledgements

Special thanks to the open-source community and the contributors of the libraries and frameworks used in this project.

---

For any questions or support, please contact spencerinc.dev@gmail.com(mailto:spencerinc.dev@gmail.com). 
