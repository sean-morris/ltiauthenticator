from unittest.mock import patch

import jwt

from ltiauthenticator.lti13.auth import LTI13Authenticator


class MockLTI13Authenticator(LTI13Authenticator):
    """Mocks the LTI13Authenticator for testing.

    Args:
        LTI13Authenticator (OAuthenticator): The LTI13Authenticator used for mocking.
    """

    auto_login = True
    login_service = "LTI 1.3"
    username_key = "email"
    client_id = "abc123"
    config_url = "/lti13/config"
    authorize_url = "https://my.platform.domain/api/lti/authorize_redirect"
    jwks_endpoint = "https://my.platform.domain"
    token_url = "https://my.platform.domain/login/oauth2/token"
    jwks_algorithms = ["RS256"]
    issuer = "https://my.platform.domain"


def patched_jwk_client(response):
    return patch.object(jwt.PyJWKClient, "fetch_data", return_value=response)
