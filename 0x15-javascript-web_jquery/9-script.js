#!/usr/bin/node
/* global $ */
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
    $('div#hello').text(response.hello)
  })
});
