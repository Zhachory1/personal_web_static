load("@build_bazel_rules_nodejs//:index.bzl", "pkg_web")

pkg_web(
    name = "public",
    srcs = [
        "favicon.ico",
        "index.html",
        "sitemap.xml",
        "ZhachResume.pdf",
        "//new_public/css:bootstrap.min.css",
        "//new_public/scss:styles",
        "//new_public/js:main_bin",
        "//new_public/libs:libs",
        "//new_public/images:images"
    ],
    visibility = [
        "//:__pkg__",
    ],
)

exports_files([
    "package.json",
    "package-lock.json"
])