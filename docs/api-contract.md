cat > docs/api-contract.md << 'EOF'
# API Contract (v1)

Base URL: /api/v1

## POST /schedule/generate
Generate a recommended schedule for one task.

### Request (JSON)
{
  "taskName": "string",
  "deadline": "YYYY-MM-DD",
  "expectedOutcome": "string",
  "hoursPerWeek": 5,
  "workingStyle": "deep_work|pomodoro|light",
  "startDate": "YYYY-MM-DD"
}

### Response (JSON)
{
  "taskName": "string",
  "startDate": "YYYY-MM-DD",
  "deadline": "YYYY-MM-DD",
  "hoursPerWeek": 5,
  "workingStyle": "string",
  "schedule": [
    {
      "date": "YYYY-MM-DD",
      "minutes": 60,
      "focus": "string"
    }
  ]
}

### Notes
- v1 should not require auth.
- v1 schedule can be rule-based (even split of hours until deadline).
- Later: add "reasoning" field + LLM suggestions.
EOF
