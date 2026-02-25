package main

import (
	"log"

	"central-server/api"
	"central-server/storage"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	godotenv.Load()
	storage.ConnectDB()
	storage.StartDBWorker() // starts insert goroutine

	r := gin.Default()
	r.POST("/ingest", api.IngestLog)

	log.Println("Central Log Server running on :8080")
	r.Run(":8080")
}
