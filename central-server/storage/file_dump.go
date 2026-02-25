package storage

import (
	"encoding/json"
	"os"

	"central-server/queue"
)

func StartFileDump() {
	go func() {
		f, _ := os.OpenFile("logs_dump.json", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)
		defer f.Close()

		encoder := json.NewEncoder(f)

		for logItem := range queue.LogBuffer {
			encoder.Encode(logItem)
		}
	}()
}
