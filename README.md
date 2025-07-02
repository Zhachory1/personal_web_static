# personal_web
My personal website, but only the static files. I will have the precompiled files in the src folder and the compiled ones in the public folder.

# Status
Currently working with a BASIC page.

# Notes
## Firewall
For the server, make sure you set up the firewall correctly to test:

```
ufw enable
ufw allow 8080

... Do you testing

ufw reset
ufw disable
```

## SSL Setup
This was the worst headache.

Followed the guide here:

https://www.digitalocean.com/community/tutorials/how-to-secure-a-containerized-node-js-application-with-nginx-let-s-encrypt-and-docker-compose

We basically set up a docker-compose to run nginx as a proxy to serve and load balance and route things.

Also has instructions to recreate certifications when they expire.

