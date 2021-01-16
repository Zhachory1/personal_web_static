load("@rules_pkg//:pkg.bzl", "pkg_tar", "pkg_deb")
load("@io_bazel_rules_docker//container:container.bzl", "container_image", "container_push")

genrule(
    name = "pull_index_to_root",
    srcs = ["//new_public:public"],
    outs = ["index.html"],
    cmd = "cat $(locations //new_public:public)/index.html > $@",
)

genrule(
    name = "pull_favicon_to_root",
    srcs = ["//new_public:public"],
    outs = ["favicon.ico"],
    cmd = "cat $(locations //new_public:public)/favicon.ico > $@",
)

pkg_tar(
    name = "web_server_tar",
    extension = "tar.gz",
    srcs = [
        ":pull_favicon_to_root",
        ":pull_index_to_root",
        "//server",
        "//new_public:public",
    ],
    mode = "0755",
)

container_image(
    name = "web_server_image",
    base = "@alpine_linux_amd64//image",
    # entrypoint = ["./server"],
    tars = [":web_server_tar"],
)

container_push(
    name = "web_server-push",
    format = "Docker",
    image = ":web_server_image",
    registry = "index.docker.io",
    repository = "zhachory1/perso-web-server",
)