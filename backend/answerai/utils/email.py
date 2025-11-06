import logging
import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional

from answerai.env import SRC_LOG_LEVELS, ANSWERAI_NAME

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS.get("MAIN", "INFO"))


def generate_verification_token() -> str:
    """
    Generate a secure random token for email verification.
    Returns a 32-character hexadecimal string.
    """
    return secrets.token_hex(32)


def send_verification_email(
    email: str,
    token: str,
    smtp_host: str,
    smtp_port: int,
    smtp_username: str,
    smtp_password: str,
    smtp_from_email: str,
    smtp_use_tls: bool = True,
    base_url: Optional[str] = None,
) -> bool:
    """
    Send a verification email to the user with a verification link.

    Args:
        email: The recipient's email address
        token: The verification token
        smtp_host: SMTP server hostname
        smtp_port: SMTP server port
        smtp_username: SMTP username
        smtp_password: SMTP password
        smtp_from_email: From email address
        smtp_use_tls: Whether to use TLS (default: True)
        base_url: Base URL for the verification link (optional)

    Returns:
        True if email was sent successfully, False otherwise
    """
    if not smtp_host or not smtp_from_email:
        log.error("SMTP configuration is incomplete. Cannot send verification email.")
        return False

    try:
        # Create verification URL
        if base_url:
            verification_url = f"{base_url}/auth/verify?token={token}"
        else:
            verification_url = f"/auth/verify?token={token}"

        # Create email content
        subject = f"Verify your email for {ANSWERAI_NAME}"

        # HTML email template
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Verification</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center; border-radius: 10px 10px 0 0;">
        <h1 style="color: white; margin: 0; font-size: 28px;">Welcome to {ANSWERAI_NAME}!</h1>
    </div>

    <div style="background-color: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <h2 style="color: #667eea; margin-top: 0;">Verify Your Email Address</h2>

        <p>Thank you for signing up! To complete your registration and start using {ANSWERAI_NAME}, please verify your email address by clicking the button below:</p>

        <div style="text-align: center; margin: 30px 0;">
            <a href="{verification_url}"
               style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                      color: white;
                      padding: 15px 40px;
                      text-decoration: none;
                      border-radius: 5px;
                      font-weight: bold;
                      display: inline-block;
                      box-shadow: 0 4px 6px rgba(102, 126, 234, 0.4);">
                Verify Email Address
            </a>
        </div>

        <p>Or copy and paste this link into your browser:</p>
        <p style="background-color: #e9ecef; padding: 15px; border-radius: 5px; word-break: break-all; font-size: 14px;">
            {verification_url}
        </p>

        <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">

        <p style="color: #666; font-size: 14px; margin-bottom: 0;">
            If you didn't create an account with {ANSWERAI_NAME}, you can safely ignore this email.
        </p>
    </div>

    <div style="text-align: center; margin-top: 20px; color: #999; font-size: 12px;">
        <p>© {ANSWERAI_NAME}. All rights reserved.</p>
    </div>
</body>
</html>
"""

        # Plain text version for email clients that don't support HTML
        text_content = f"""
Welcome to {ANSWERAI_NAME}!

Thank you for signing up! To complete your registration and start using {ANSWERAI_NAME},
please verify your email address by visiting the following link:

{verification_url}

If you didn't create an account with {ANSWERAI_NAME}, you can safely ignore this email.

© {ANSWERAI_NAME}. All rights reserved.
"""

        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = smtp_from_email
        message["To"] = email

        # Attach both plain text and HTML versions
        part1 = MIMEText(text_content, "plain")
        part2 = MIMEText(html_content, "html")
        message.attach(part1)
        message.attach(part2)

        # Send email
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            if smtp_use_tls:
                server.starttls()

            if smtp_username and smtp_password:
                server.login(smtp_username, smtp_password)

            server.send_message(message)

        log.info(f"Verification email sent successfully to {email}")
        return True

    except smtplib.SMTPAuthenticationError:
        log.error("SMTP authentication failed. Check username and password.")
        return False
    except smtplib.SMTPException as e:
        log.error(f"SMTP error occurred while sending verification email: {e}")
        return False
    except Exception as e:
        log.exception(f"Unexpected error sending verification email: {e}")
        return False


def send_password_reset_email(
    email: str,
    token: str,
    smtp_host: str,
    smtp_port: int,
    smtp_username: str,
    smtp_password: str,
    smtp_from_email: str,
    smtp_use_tls: bool = True,
    base_url: Optional[str] = None,
) -> bool:
    """
    Send a password reset email to the user.
    This function is provided for future use.
    """
    # Implementation for password reset emails can be added here if needed
    pass
