def get_mock_memory_data():
    """
    Returns a list of mock memory data dictionaries for testing the Memory Card UI.
    """
    return [
        {
            "id": "mem_001",
            "document": "Effective March 1st, 2024, the company allows WFH up to 2 days/week. This policy applies to all full-time employees who have completed their probation period. Requests must be submitted by Tuesday for the following week.",
            "metadata": {
                "title": "WFH Policy 2024",
                "status": "active",
                "created_at": "2026-02-17",
                "source": "HR_Manual.pdf",
                "confidence": 0.92
            }
        },
        {
            "id": "mem_002",
            "document": "The Q1 2024 All-Hands meeting is scheduled for April 15th at 10:00 AM in the main conference room. Lunch will be provided.",
            "metadata": {
                "title": "Q1 2024 All-Hands",
                "status": "expiring",
                "created_at": "2026-01-10",
                "source": "Email_Blast",
                "confidence": 0.98
            }
        },
         {
            "id": "mem_003",
            "document": "Legacy project 'Titan' has been deprecated. All resources should be moved to 'Project Atlas' by end of Q2. Please refer to the migration guide for details.",
            "metadata": {
                "title": "Project Titan Deprecation",
                "status": "archived",
                "created_at": "2025-11-05",
                "source": "Meeting_Notes_Nov.docx",
                "confidence": 0.85
            }
        }
    ]
