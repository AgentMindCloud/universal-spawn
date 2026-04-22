# Build stage.
FROM golang:1.23 AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o /out/your-cli ./cmd/your-cli

# Distroless runtime.
FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/your-cli /usr/local/bin/your-cli
USER nonroot:nonroot
ENTRYPOINT ["/usr/local/bin/your-cli"]
