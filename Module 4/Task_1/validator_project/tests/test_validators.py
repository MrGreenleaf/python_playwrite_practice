class EmailValidator:
    def is_valid(self, email):
        if not email or "@" not in email:
            return False

        parts = email.split("@")
        if len(parts) != 2:
            return False

        username, domain = parts
        if not username or not domain or "." not in domain:
            return False

        return True