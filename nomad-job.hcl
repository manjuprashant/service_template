job "service" {
  datacenters = ["dc1"]
  group "service-group" {
    task "service" {
      driver = "docker"
      config {
        image = "your-image:latest"
        port_map {
          http = 8000
        }
      }
      resources {
        cpu    = 500
        memory = 256
      }
    }
  }
}
