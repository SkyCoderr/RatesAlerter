const sendmail = require('sendmail')();

sendmail({
    from: 'fragrancefarter@protonmail.com',
    password: 'asdf12',
    to: 'jayonwead@yahoo.com',
    cc: 'mir2014@foxmail.com',
    subject: 'Email Test',
    html: 'Hello',
  }, function(err, reply) {
    console.log(err && err.stack);
    console.dir(reply);
});