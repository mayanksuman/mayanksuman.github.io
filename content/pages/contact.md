---
layout: page
title: Contact
disable_comments: true
disable_share: true
---

<!--
     Before implementing this contact form make sure
     1. you verify your form on formspree.io.
-->

<form id="my-form" class="wj-contact" action="https://formspree.io/xqkynjnj" method="POST">
	<input type="text" name="email" placeholder="Email Address">
    <input type="text" name="name" placeholder="Name (Optional)">
    <textarea type="text" name="content" rows="10" placeholder="Message"></textarea>
    <input type="submit" value="Submit" id="my-form-button">
	<p id="my-form-status"></p>
</form>



<script>
  window.addEventListener("DOMContentLoaded", function() {

    // get the form elements defined in your form HTML above

    var form = document.getElementById("my-form");
    var button = document.getElementById("my-form-button");
    var status = document.getElementById("my-form-status");

    // Success and Error functions for after the form is submitted

    function success() {
      form.reset();
      button.style = "display: none ";
      status.innerHTML = "Thanks!";
    }

    function error() {
      status.innerHTML = "Oops! There was a problem.";
    }

    // handle the form submission event

    form.addEventListener("submit", function(ev) {
      ev.preventDefault();
      var data = new FormData(form);
	  if (data.get("email") == "" || data.get("content").trim() == "") {
		alert("Please fill both your email and message.");
	  }else{
		if (validateEmail(data.get("email"))){
		  ajax(form.method, form.action, data, success, error);}
	  }
    });
  });

  // helper function for sending an AJAX request

  function ajax(method, url, data, success, error) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.onreadystatechange = function() {
      if (xhr.readyState !== XMLHttpRequest.DONE) return;
      if (xhr.status === 200) {
        success(xhr.response, xhr.responseType);
      } else {
        error(xhr.status, xhr.response, xhr.responseType);
      }
    };
    xhr.send(data);
  }

  // helper function for checking validity of email string

  function validateEmail(mail) {
	if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)){
    return (true);
	}
	alert("Please enter a valid email address!");
    return (false);
  }
</script>

<style>
form.wj-contact input[type="text"], form.wj-contact textarea[type="text"] {
    width: 100%;
    vertical-align: middle;
    margin-top: 0.25em;
    margin-bottom: 0.5em;
    padding: 0.75em;
    font-family: monospace, sans-serif;
    font-weight: lighter;
    border-style: solid;
    border-color: #444;
    outline-color: #2e83e6;
    border-width: 1px;
    border-radius: 3px;
    transition: box-shadow .2s ease;
}

form.wj-contact input[type="submit"] {
    outline: none;
    color: white;
    background-color: #2e83e6;
    border-radius: 3px;
    padding: 0.5em;
    margin: 0.25em 0 0 0;
    border: 1px solid transparent;
    height: auto;
}
</style>
