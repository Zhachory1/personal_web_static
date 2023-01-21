load("@build_bazel_rules_nodejs//:index.bzl", "pkg_web")

pkg_web(
    name = "public",
    srcs = [
        "favicon.ico",
        "index.html",
        "sitemap.xml",
        "ZhachResume.pdf",
        "//public/css:bootstrap.min.css",
        "//public/scss:styles",
        "//public/js:main_bin",
        "//public/libs:libs",
        "//public/images:images"
    ],
    visibility = [
        "//:__pkg__",
    ],
)

exports_files([
    "package.json",
    "package-lock.json"
])