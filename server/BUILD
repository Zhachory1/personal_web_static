load("@io_bazel_rules_go//go:def.bzl", "go_binary")

go_binary(
    name = "server",
    srcs = ["server.go"],
    data = ["//public"],
    visibility = ["//:__pkg__"]
)