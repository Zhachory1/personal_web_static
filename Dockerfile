# Base Image
FROM bazelbuild/bazel:latest AS builder

# Working Directory
WORKDIR /app

# Copy the project files
COPY . .

# Build the project with Bazel
RUN bazel build //:web_server_tar

# Create a runtime image
FROM launcher.gcr.io/google/debian9:latest

# Copy the built artifact from the builder image
COPY --from=builder /app/bazel-bin/web_server_tar /app/web_server_tar

# Set the entrypoint
ENTRYPOINT ["/app/web_server_tar/server"]