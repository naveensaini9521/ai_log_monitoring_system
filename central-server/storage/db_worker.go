package storage

import (
	"context"
	"log"

	"central-server/queue"
)

func StartDBWorker() {
	go func() {
		log.Println("✅ DB worker started")

		for logItem := range queue.LogBuffer {
			log.Println("📥 DB worker received log:", logItem.Message)

			_, err := DB.Exec(
				context.Background(),
				`INSERT INTO public.logs
				 (level, message, source, service, host, raw_log)
				 VALUES ($1,$2,$3,$4,$5,$6)`,
				logItem.Level,
				logItem.Message,
				logItem.Source,
				logItem.Service,
				logItem.Host,
				logItem.RawLog,
			)

			if err != nil {
				log.Println("❌ DB insert failed:", err)
			} else {
				log.Println("✅ Log inserted into DB")
			}
		}
	}()
}
