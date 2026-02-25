package queue

import "central-server/models"

var LogBuffer = make(chan models.Log, 1000)
