package api

import (
	"log"
	"net/http"

	"central-server/models"
	"central-server/queue"

	"github.com/gin-gonic/gin"
)

func IngestLog(c *gin.Context) {
	var logItem models.Log // ✅ renamed variable

	if err := c.ShouldBindJSON(&logItem); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	log.Println("📤 Ingest received log:", logItem.Message)

	queue.LogBuffer <- logItem

	log.Println("➡️ Log pushed into channel")

	c.JSON(http.StatusOK, gin.H{"status": "log accepted"})
}
