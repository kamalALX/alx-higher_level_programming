#!/usr/bin/node
/* global $ */
$(document).ready(function () {
  $('div#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
