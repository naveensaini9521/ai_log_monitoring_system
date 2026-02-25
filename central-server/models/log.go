package models

type Log struct {
	Timestamp string `json:"timestamp"`
	Level     string `json:"level"`
	Message   string `json:"message"`
	Source    string `json:"source"`
	Service   string `json:"service"`
	Host      string `json:"host"`
	RawLog    string `json:"raw_log"`
}
