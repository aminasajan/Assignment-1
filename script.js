// Define exchange rates in an object
// For simplicity, these are rates from USD to other currencies.
var exchangeRates = {
    "USD_USD": 1.0,
    "USD_INR": 74.0,
    "USD_EUR": 0.85,
    "USD_OMR": 0.385,
    "USD_GBP": 0.75,
    "USD_CAD": 1.25,
    "USD_AUD": 1.35,
  };
  
  // Function to Convert Currency
  function convertCurrency() {
    var fromCurrency = document.getElementById("fromCurrency").value;
    var toCurrency = document.getElementById("toCurrency").value;
    var amount = document.getElementById("amount").value;
  
    var fromRate = exchangeRates["USD_" + fromCurrency];
    var toRate = exchangeRates["USD_" + toCurrency];
  
    var result = (amount / fromRate) * toRate;
    
    if (isNaN(result)) {
      document.getElementById("result").innerText = "Invalid conversion";
    } else {
      document.getElementById("result").innerText = `${amount} ${fromCurrency} = ${result.toFixed(2)} ${toCurrency}`;
    }
  }
  