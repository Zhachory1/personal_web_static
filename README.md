# personal_web
My personal website with a golang server and simple html pages. Future work would be to visualize my projects into this site.

# Status
Currently working with a BASIC page.

# To run
Make sure you have bazel installed and run the following command:

```
bazel run server
```

This will bring up a local server which you can access at localhost:8080

# Common tasks

If you have bazel, please add the following alias to your rc file:

```
alias please="bazel"
```

If you don't have this, you're doing it wrong.

### To build a tarball
`please run -c opt :web_server_tar`

### To build a docker image
`please run -c opt :web_server_image`

### To push docker image to the repo
`please run -c opt :web_server-push`

With these commands, I can test locally, test with a docker binary, and release things into docker.

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

