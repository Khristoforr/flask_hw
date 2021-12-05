

AD_CREATE = {
	"type": "object",
	"properties": {
		"title": {
			"type": "string"
		},
		"description": {
			"type": "string",
		},
		"owner": {
			"type": "string",
		},
		"creation_date": {
			"type": "string",
			"pattern": "^\d{4}-\d{2}-\d{2}$"
		}
	},
	"required": ["title", "owner", "creation_date"]
}
