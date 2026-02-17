# pipeshub-sdk
pipeshub-sdk is the official python client library for integrating Pipeshub into your product and internal tools

<!-- Start Summary [summary] -->
## Summary

PipesHub API: Unified API documentation for PipesHub services.

PipesHub is an enterprise-grade platform providing:
- User authentication and management
- Document storage and version control
- Knowledge base management
- Enterprise search and conversational AI
- Third-party integrations via connectors
- System configuration management
- Crawling job scheduling
- Email services

## Authentication
Most endpoints require JWT Bearer token authentication. Some internal endpoints use scoped tokens for service-to-service communication.

## Base URLs
All endpoints use the `/api/v1` prefix unless otherwise noted.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [pipeshub-sdk](#pipeshub-sdk)
  * [Authentication](#authentication)
  * [Base URLs](#base-urls)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication-1)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Server-sent event streaming](#server-sent-event-streaming)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from pipeshub python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pipeshub",
# ]
# ///

from pipeshub import Pipeshub

sdk = Pipeshub(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.init_auth(email="user@example.com")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from pipeshub import Pipeshub

async def main():

    async with Pipeshub(
        server_url="https://api.example.com",
    ) as p_client:

        res = await p_client.user_account.init_auth_async(email="user@example.com")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      | Environment Variable   |
| ------------- | ---- | ----------- | ---------------------- |
| `bearer_auth` | http | HTTP Bearer | `PIPESHUB_BEARER_AUTH` |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.user_account.init_auth(email="user@example.com")

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import os
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.reset_password_token(security=models.ResetPasswordWithTokenSecurity(
        scoped_token=os.getenv("PIPESHUB_SCOPED_TOKEN", ""),
    ), password="H9GEHoL829GXj06")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [AgentConversations](docs/sdks/agentconversations/README.md)

* [list](docs/sdks/agentconversations/README.md#list) - List agent conversations
* [create](docs/sdks/agentconversations/README.md#create) - Create agent conversation
* [stream](docs/sdks/agentconversations/README.md#stream) - Create agent conversation with streaming
* [get](docs/sdks/agentconversations/README.md#get) - Get agent conversation
* [delete](docs/sdks/agentconversations/README.md#delete) - Delete agent conversation
* [add_message](docs/sdks/agentconversations/README.md#add_message) - Add message to agent conversation
* [stream_message](docs/sdks/agentconversations/README.md#stream_message) - Add message with streaming
* [regenerate_response](docs/sdks/agentconversations/README.md#regenerate_response) - Regenerate agent response

### [Agents](docs/sdks/agents/README.md)

* [get_all](docs/sdks/agents/README.md#get_all) - List agents
* [create](docs/sdks/agents/README.md#create) - Create agent
* [get_tools](docs/sdks/agents/README.md#get_tools) - List available tools
* [get](docs/sdks/agents/README.md#get) - Get agent
* [update](docs/sdks/agents/README.md#update) - Update agent
* [delete](docs/sdks/agents/README.md#delete) - Delete agent
* [get_permissions](docs/sdks/agents/README.md#get_permissions) - Get agent permissions
* [update_permissions](docs/sdks/agents/README.md#update_permissions) - Update agent permissions
* [share](docs/sdks/agents/README.md#share) - Share agent
* [unshare](docs/sdks/agents/README.md#unshare) - Revoke agent access

### [AgentTemplates](docs/sdks/agenttemplates/README.md)

* [list](docs/sdks/agenttemplates/README.md#list) - List agent templates
* [create](docs/sdks/agenttemplates/README.md#create) - Create agent template
* [get_template](docs/sdks/agenttemplates/README.md#get_template) - Get agent template
* [update](docs/sdks/agenttemplates/README.md#update) - Update agent template
* [delete](docs/sdks/agenttemplates/README.md#delete) - Delete agent template

### [AiModelsConfiguration](docs/sdks/aimodelsconfiguration/README.md)

* [create](docs/sdks/aimodelsconfiguration/README.md#create) - Bulk create AI models configuration
* [get](docs/sdks/aimodelsconfiguration/README.md#get) - Get all AI models configuration

### [AiModelsProviders](docs/sdks/aimodelsproviders/README.md)

* [list](docs/sdks/aimodelsproviders/README.md#list) - Get all AI model providers
* [get_by_type](docs/sdks/aimodelsproviders/README.md#get_by_type) - Get models by type
* [get_available_by_type](docs/sdks/aimodelsproviders/README.md#get_available_by_type) - Get available models for selection
* [add](docs/sdks/aimodelsproviders/README.md#add) - Add new AI model provider
* [update](docs/sdks/aimodelsproviders/README.md#update) - Update AI model provider
* [delete](docs/sdks/aimodelsproviders/README.md#delete) - Delete AI model provider
* [set_default](docs/sdks/aimodelsproviders/README.md#set_default) - Set default AI model

### [AuthConfig](docs/sdks/authconfigsdk/README.md)

* [set_azure_ad](docs/sdks/authconfigsdk/README.md#set_azure_ad) - Configure Azure AD authentication
* [set_sso](docs/sdks/authconfigsdk/README.md#set_sso) - Configure SAML SSO authentication
* [get_sso](docs/sdks/authconfigsdk/README.md#get_sso) - Get SAML SSO configuration

### [AuthenticationConfiguration](docs/sdks/authenticationconfiguration/README.md)

* [set_microsoft](docs/sdks/authenticationconfiguration/README.md#set_microsoft) - Configure Microsoft authentication
* [get_microsoft](docs/sdks/authenticationconfiguration/README.md#get_microsoft) - Get Microsoft authentication configuration
* [set_google](docs/sdks/authenticationconfiguration/README.md#set_google) - Configure Google authentication
* [get_google](docs/sdks/authenticationconfiguration/README.md#get_google) - Get Google authentication configuration
* [set_o_auth_config](docs/sdks/authenticationconfiguration/README.md#set_o_auth_config) - Configure generic OAuth provider

### [AuthenticationConfigurations](docs/sdks/authenticationconfigurations/README.md)

* [get_azure_ad](docs/sdks/authenticationconfigurations/README.md#get_azure_ad) - Get Azure AD configuration
* [get_generic_o_auth_config](docs/sdks/authenticationconfigurations/README.md#get_generic_o_auth_config) - Get generic OAuth configuration

### [Connector](docs/sdks/connector/README.md)

* [reindex_record](docs/sdks/connector/README.md#reindex_record) - Reindex single record
* [reindex_record_group](docs/sdks/connector/README.md#reindex_record_group) - Reindex record group
* [reindex_failed_records](docs/sdks/connector/README.md#reindex_failed_records) - Reindex failed connector records
* [get_stats](docs/sdks/connector/README.md#get_stats) - Get connector statistics

### [ConnectorConfiguration](docs/sdks/connectorconfiguration/README.md)

* [update_config](docs/sdks/connectorconfiguration/README.md#update_config) - Update connector configuration
* [update_auth_config](docs/sdks/connectorconfiguration/README.md#update_auth_config) - Update authentication configuration
* [get_google_workspace_credentials](docs/sdks/connectorconfiguration/README.md#get_google_workspace_credentials) - Get Google Workspace credentials status

### [ConnectorConfigurations](docs/sdks/connectorconfigurations/README.md)

* [get](docs/sdks/connectorconfigurations/README.md#get) - Get connector configuration
* [update_filters_sync](docs/sdks/connectorconfigurations/README.md#update_filters_sync) - Update filters and sync configuration

### [ConnectorControls](docs/sdks/connectorcontrols/README.md)

* [toggle](docs/sdks/connectorcontrols/README.md#toggle) - Toggle connector sync or agent

### [ConnectorFilters](docs/sdks/connectorfilters/README.md)

* [get](docs/sdks/connectorfilters/README.md#get) - Get filter options
* [save](docs/sdks/connectorfilters/README.md#save) - Save filter selections
* [get_options](docs/sdks/connectorfilters/README.md#get_options) - Get dynamic filter options

### [ConnectorInstances](docs/sdks/connectorinstances/README.md)

* [list](docs/sdks/connectorinstances/README.md#list) - List connector instances
* [create](docs/sdks/connectorinstances/README.md#create) - Create connector instance
* [list_active](docs/sdks/connectorinstances/README.md#list_active) - List active connector instances
* [list_inactive](docs/sdks/connectorinstances/README.md#list_inactive) - List inactive connector instances
* [list_configured](docs/sdks/connectorinstances/README.md#list_configured) - List configured connector instances
* [list_active_agents](docs/sdks/connectorinstances/README.md#list_active_agents) - List active agent connectors
* [get](docs/sdks/connectorinstances/README.md#get) - Get connector instance
* [delete](docs/sdks/connectorinstances/README.md#delete) - Delete connector instance
* [update_name](docs/sdks/connectorinstances/README.md#update_name) - Update connector instance name

### [ConnectorOAuth](docs/sdks/connectoroauth/README.md)

* [exchange_code_for_token](docs/sdks/connectoroauth/README.md#exchange_code_for_token) - Exchange authorization code for tokens (legacy)
* [get_authorization_url](docs/sdks/connectoroauth/README.md#get_authorization_url) - Get OAuth authorization URL
* [handle_callback](docs/sdks/connectoroauth/README.md#handle_callback) - OAuth callback handler

### [ConnectorOauthConfiguration](docs/sdks/connectoroauthconfiguration2/README.md)

* [get_google_workspace](docs/sdks/connectoroauthconfiguration2/README.md#get_google_workspace) - Get Google Workspace OAuth configuration
* [set_atlassian_config](docs/sdks/connectoroauthconfiguration2/README.md#set_atlassian_config) - Configure Atlassian OAuth
* [set_one_drive_config](docs/sdks/connectoroauthconfiguration2/README.md#set_one_drive_config) - Configure OneDrive connector

### [ConnectorOAuthConfiguration](docs/sdks/connectoroauthconfiguration1/README.md)

* [create_google_workspace_credentials](docs/sdks/connectoroauthconfiguration1/README.md#create_google_workspace_credentials) - Upload Google Workspace credentials
* [set_google_workspace](docs/sdks/connectoroauthconfiguration1/README.md#set_google_workspace) - Configure Google Workspace OAuth
* [get_atlassian_config](docs/sdks/connectoroauthconfiguration1/README.md#get_atlassian_config) - Get Atlassian OAuth configuration
* [get_one_drive_config](docs/sdks/connectoroauthconfiguration1/README.md#get_one_drive_config) - Get OneDrive configuration

### [ConnectorOAuthConfigurations](docs/sdks/connectoroauthconfigurations/README.md)

* [set_share_point](docs/sdks/connectoroauthconfigurations/README.md#set_share_point) - Configure SharePoint connector
* [get_share_point](docs/sdks/connectoroauthconfigurations/README.md#get_share_point) - Get SharePoint configuration

### [ConnectorRegistry](docs/sdks/connectorregistry/README.md)

* [list](docs/sdks/connectorregistry/README.md#list) - List available connector types
* [get_schema](docs/sdks/connectorregistry/README.md#get_schema) - Get connector configuration schema

### [Connectors](docs/sdks/connectors/README.md)

* [resync](docs/sdks/connectors/README.md#resync) - Resync connector

### [ConnectorService](docs/sdks/connectorservice/README.md)

* [health_check](docs/sdks/connectorservice/README.md#health_check) - [Connector Service] Health check
* [google_drive_webhook](docs/sdks/connectorservice/README.md#google_drive_webhook) - [Connector Service] Google Drive webhook
* [get_internal_stream_record](docs/sdks/connectorservice/README.md#get_internal_stream_record) - [Connector Service] Internal stream record
* [convert_record_buffer](docs/sdks/connectorservice/README.md#convert_record_buffer) - [Connector Service] Convert record buffer
* [get_stats](docs/sdks/connectorservice/README.md#get_stats) - [Connector Service] Get connector statistics
* [reindex_failed_records](docs/sdks/connectorservice/README.md#reindex_failed_records) - [Connector Service] Reindex all failed records
* [get_signed_url](docs/sdks/connectorservice/README.md#get_signed_url) - [Connector Service] Get signed URL for record

### [Conversations](docs/sdks/conversations/README.md)

* [create](docs/sdks/conversations/README.md#create) - Create a new AI conversation
* [create_with_streaming](docs/sdks/conversations/README.md#create_with_streaming) - Create conversation with streaming response
* [list](docs/sdks/conversations/README.md#list) - List all conversations
* [list_archived](docs/sdks/conversations/README.md#list_archived) - List archived conversations
* [get_by_id](docs/sdks/conversations/README.md#get_by_id) - Get conversation by ID
* [delete](docs/sdks/conversations/README.md#delete) - Delete conversation
* [add_message](docs/sdks/conversations/README.md#add_message) - Add message to conversation
* [add_message_stream](docs/sdks/conversations/README.md#add_message_stream) - Add message with streaming response
* [share](docs/sdks/conversations/README.md#share) - Share conversation with users
* [unshare](docs/sdks/conversations/README.md#unshare) - Revoke conversation access
* [update_title](docs/sdks/conversations/README.md#update_title) - Update conversation title
* [archive](docs/sdks/conversations/README.md#archive) - Archive conversation
* [unarchive](docs/sdks/conversations/README.md#unarchive) - Unarchive conversation
* [regenerate](docs/sdks/conversations/README.md#regenerate) - Regenerate AI response
* [submit_feedback](docs/sdks/conversations/README.md#submit_feedback) - Submit feedback on AI response

### [CrawlingJobs](docs/sdks/crawlingjobs/README.md)

* [schedule](docs/sdks/crawlingjobs/README.md#schedule) - Schedule a crawling job
* [get_status](docs/sdks/crawlingjobs/README.md#get_status) - Get crawling job status
* [remove](docs/sdks/crawlingjobs/README.md#remove) - Remove a crawling job
* [pause](docs/sdks/crawlingjobs/README.md#pause) - Pause a crawling job
* [resume](docs/sdks/crawlingjobs/README.md#resume) - Resume a paused crawling job
* [list_all_statuses](docs/sdks/crawlingjobs/README.md#list_all_statuses) - Get all crawling job statuses
* [remove_all](docs/sdks/crawlingjobs/README.md#remove_all) - Remove all crawling jobs

### [DoclingService](docs/sdks/doclingservice/README.md)

* [get_health](docs/sdks/doclingservice/README.md#get_health) - [Docling Service] Health check
* [process_pdf](docs/sdks/doclingservice/README.md#process_pdf) - [Docling Service] Process PDF document
* [parse_pdf](docs/sdks/doclingservice/README.md#parse_pdf) - [Docling Service] Parse PDF (Phase 1)

### [DoclingServices](docs/sdks/doclingservices/README.md)

* [create_blocks](docs/sdks/doclingservices/README.md#create_blocks) - [Docling Service] Create blocks from parse result (Phase 2)

### [DocumentBuffer](docs/sdks/documentbuffer/README.md)

* [update](docs/sdks/documentbuffer/README.md#update) - Update document buffer

### [DocumentBuffers](docs/sdks/documentbuffers/README.md)

* [get](docs/sdks/documentbuffers/README.md#get) - Get document buffer

### [DocumentManagement](docs/sdks/documentmanagement/README.md)

* [get_by_id](docs/sdks/documentmanagement/README.md#get_by_id) - Get document by ID
* [delete_by_id](docs/sdks/documentmanagement/README.md#delete_by_id) - Delete document
* [download](docs/sdks/documentmanagement/README.md#download) - Download document

### [DocumentUpload](docs/sdks/documentupload/README.md)

* [upload](docs/sdks/documentupload/README.md#upload) - Upload a new document
* [create_placeholder](docs/sdks/documentupload/README.md#create_placeholder) - Create document placeholder
* [get_direct_url](docs/sdks/documentupload/README.md#get_direct_url) - Get direct upload URL

### [EmailOperations](docs/sdks/emailoperations/README.md)

* [send](docs/sdks/emailoperations/README.md#send) - Send a transactional email

### [Folders](docs/sdks/folders/README.md)

* [create_root](docs/sdks/folders/README.md#create_root) - Create root folder
* [get_contents](docs/sdks/folders/README.md#get_contents) - Get folder contents
* [update](docs/sdks/folders/README.md#update) - Update folder
* [delete](docs/sdks/folders/README.md#delete) - Delete folder
* [create_sub](docs/sdks/folders/README.md#create_sub) - Create subfolder

### [IndexingServices](docs/sdks/indexingservices/README.md)

* [get_health](docs/sdks/indexingservices/README.md#get_health) - [Indexing Service] Health check

### [KnowledgeBases](docs/sdks/knowledgebases/README.md)

* [create](docs/sdks/knowledgebases/README.md#create) - Create a new knowledge base
* [list](docs/sdks/knowledgebases/README.md#list) - List all knowledge bases
* [get](docs/sdks/knowledgebases/README.md#get) - Get knowledge base by ID
* [update](docs/sdks/knowledgebases/README.md#update) - Update knowledge base
* [delete](docs/sdks/knowledgebases/README.md#delete) - Delete knowledge base
* [get_root_nodes](docs/sdks/knowledgebases/README.md#get_root_nodes) - Get knowledge hub root nodes
* [get_child_nodes](docs/sdks/knowledgebases/README.md#get_child_nodes) - Get knowledge hub child nodes

### [MailConfigurations](docs/sdks/mailconfigurations/README.md)

* [reload_smtp](docs/sdks/mailconfigurations/README.md#reload_smtp) - Reload SMTP configuration

### [MetricsCollection](docs/sdks/metricscollection/README.md)

* [get_config](docs/sdks/metricscollection/README.md#get_config) - Get metrics collection configuration
* [toggle](docs/sdks/metricscollection/README.md#toggle) - Enable or disable metrics collection
* [set_push_interval](docs/sdks/metricscollection/README.md#set_push_interval) - Configure metrics push interval
* [set_server_url](docs/sdks/metricscollection/README.md#set_server_url) - Configure metrics server URL

### [Oauth](docs/sdks/oauthsdk/README.md)

* [exchange_code](docs/sdks/oauthsdk/README.md#exchange_code) - Exchange OAuth authorization code for tokens

### [OauthApps](docs/sdks/oauthapps/README.md)

* [list](docs/sdks/oauthapps/README.md#list) - List OAuth apps
* [create](docs/sdks/oauthapps/README.md#create) - Create OAuth app
* [list_scopes](docs/sdks/oauthapps/README.md#list_scopes) - List available scopes
* [get](docs/sdks/oauthapps/README.md#get) - Get OAuth app details
* [update](docs/sdks/oauthapps/README.md#update) - Update OAuth app
* [delete](docs/sdks/oauthapps/README.md#delete) - Delete OAuth app
* [regenerate_secret](docs/sdks/oauthapps/README.md#regenerate_secret) - Regenerate client secret
* [suspend](docs/sdks/oauthapps/README.md#suspend) - Suspend OAuth app
* [activate](docs/sdks/oauthapps/README.md#activate) - Activate suspended OAuth app
* [list_tokens](docs/sdks/oauthapps/README.md#list_tokens) - List app tokens
* [revoke_all_tokens](docs/sdks/oauthapps/README.md#revoke_all_tokens) - Revoke all app tokens

### [OauthConfiguration](docs/sdks/oauthconfiguration/README.md)

* [list_registry](docs/sdks/oauthconfiguration/README.md#list_registry) - List OAuth-capable connector types
* [get_connector_type](docs/sdks/oauthconfiguration/README.md#get_connector_type) - Get OAuth connector type details
* [list](docs/sdks/oauthconfiguration/README.md#list) - List OAuth configurations
* [list_by_type](docs/sdks/oauthconfiguration/README.md#list_by_type) - List OAuth configs for connector type
* [create](docs/sdks/oauthconfiguration/README.md#create) - Create OAuth configuration
* [get](docs/sdks/oauthconfiguration/README.md#get) - Get OAuth configuration
* [update](docs/sdks/oauthconfiguration/README.md#update) - Update OAuth configuration
* [delete](docs/sdks/oauthconfiguration/README.md#delete) - Delete OAuth configuration

### [OauthProvider](docs/sdks/oauthprovider/README.md)

* [authorize](docs/sdks/oauthprovider/README.md#authorize) - Initiate OAuth authorization flow
* [submit_consent](docs/sdks/oauthprovider/README.md#submit_consent) - Submit authorization consent
* [exchange_token](docs/sdks/oauthprovider/README.md#exchange_token) - Exchange authorization code for tokens
* [revoke](docs/sdks/oauthprovider/README.md#revoke) - Revoke an access or refresh token
* [introspect](docs/sdks/oauthprovider/README.md#introspect) - Introspect a token

### [OpenidConnect](docs/sdks/openidconnect1/README.md)

* [get_user_info](docs/sdks/openidconnect1/README.md#get_user_info) - Get authenticated user information

### [OpenIDConnect](docs/sdks/openidconnect2/README.md)

* [get_configuration](docs/sdks/openidconnect2/README.md#get_configuration) - OpenID Connect Discovery
* [jwks](docs/sdks/openidconnect2/README.md#jwks) - JSON Web Key Set

### [OrganizationAuthConfig](docs/sdks/organizationauthconfig/README.md)

* [update_method](docs/sdks/organizationauthconfig/README.md#update_method) - Update organization authentication methods

### [OrganizationAuthConfigs](docs/sdks/organizationauthconfigs/README.md)

* [create](docs/sdks/organizationauthconfigs/README.md#create) - Create organization authentication configuration
* [get_methods](docs/sdks/organizationauthconfigs/README.md#get_methods) - Get organization authentication methods

### [Organizations](docs/sdks/organizations/README.md)

* [check_exists](docs/sdks/organizations/README.md#check_exists) - Check if organization exists
* [create](docs/sdks/organizations/README.md#create) - Create organization
* [get](docs/sdks/organizations/README.md#get) - Get current organization
* [update](docs/sdks/organizations/README.md#update) - Update organization
* [delete](docs/sdks/organizations/README.md#delete) - Delete organization
* [upload_logo](docs/sdks/organizations/README.md#upload_logo) - Upload organization logo
* [get_logo](docs/sdks/organizations/README.md#get_logo) - Get organization logo
* [delete_logo](docs/sdks/organizations/README.md#delete_logo) - Delete organization logo
* [get_onboarding_status](docs/sdks/organizations/README.md#get_onboarding_status) - Get onboarding status
* [update_onboarding_status](docs/sdks/organizations/README.md#update_onboarding_status) - Update onboarding status

### [Permissions](docs/sdks/permissionssdk/README.md)

* [grant](docs/sdks/permissionssdk/README.md#grant) - Grant permissions
* [list](docs/sdks/permissionssdk/README.md#list) - List permissions
* [update](docs/sdks/permissionssdk/README.md#update) - Update permissions
* [delete](docs/sdks/permissionssdk/README.md#delete) - Remove permissions

### [PlatformSettings](docs/sdks/platformsettingssdk/README.md)

* [set](docs/sdks/platformsettingssdk/README.md#set) - Update platform settings
* [get](docs/sdks/platformsettingssdk/README.md#get) - Get platform settings
* [get_available_feature_flags](docs/sdks/platformsettingssdk/README.md#get_available_feature_flags) - Get available feature flags
* [set_custom_prompt](docs/sdks/platformsettingssdk/README.md#set_custom_prompt) - Update custom system prompt
* [get_custom_prompt](docs/sdks/platformsettingssdk/README.md#get_custom_prompt) - Get custom system prompt

### [PublicUrls](docs/sdks/publicurls/README.md)

* [set](docs/sdks/publicurls/README.md#set) - Set frontend public URL
* [get_frontend](docs/sdks/publicurls/README.md#get_frontend) - Get frontend public URL
* [set_connector](docs/sdks/publicurls/README.md#set_connector) - Set connector public URL
* [get_connector](docs/sdks/publicurls/README.md#get_connector) - Get connector public URL

### [QueryService](docs/sdks/queryservice/README.md)

* [check_health](docs/sdks/queryservice/README.md#check_health) - [Query Service] Health check
* [search](docs/sdks/queryservice/README.md#search) - [Query Service] Semantic search
* [chat](docs/sdks/queryservice/README.md#chat) - [Query Service] Chat with knowledge base
* [chat_stream](docs/sdks/queryservice/README.md#chat_stream) - [Query Service] Streaming chat with knowledge base
* [health_check](docs/sdks/queryservice/README.md#health_check) - [Query Service] AI model health check
* [list_tools](docs/sdks/queryservice/README.md#list_tools) - [Query Service] List available agent tools

### [QueueManagement](docs/sdks/queuemanagement/README.md)

* [get_stats](docs/sdks/queuemanagement/README.md#get_stats) - Get queue statistics

### [Records](docs/sdks/records/README.md)

* [get_all](docs/sdks/records/README.md#get_all) - Get all records across knowledge bases
* [get](docs/sdks/records/README.md#get) - Get records for a knowledge base
* [get_by_id](docs/sdks/records/README.md#get_by_id) - Get record by ID
* [update](docs/sdks/records/README.md#update) - Update record
* [delete](docs/sdks/records/README.md#delete) - Delete record
* [stream](docs/sdks/records/README.md#stream) - Stream record content
* [move](docs/sdks/records/README.md#move) - Move a record to another folder

### [Saml](docs/sdks/saml/README.md)

* [sign_in](docs/sdks/saml/README.md#sign_in) - Initiate SAML sign-in flow
* [callback](docs/sdks/saml/README.md#callback) - SAML authentication callback
* [update_app_config](docs/sdks/saml/README.md#update_app_config) - Reload SAML application configuration (Internal)

### [SemanticSearch](docs/sdks/semanticsearch/README.md)

* [post](docs/sdks/semanticsearch/README.md#post) - Perform semantic search
* [history](docs/sdks/semanticsearch/README.md#history) - Get search history
* [delete_all_history](docs/sdks/semanticsearch/README.md#delete_all_history) - Clear all search history
* [get_by_id](docs/sdks/semanticsearch/README.md#get_by_id) - Get search by ID
* [delete](docs/sdks/semanticsearch/README.md#delete) - Delete search
* [share](docs/sdks/semanticsearch/README.md#share) - Share search results
* [unshare](docs/sdks/semanticsearch/README.md#unshare) - Revoke search access
* [archive](docs/sdks/semanticsearch/README.md#archive) - Archive search
* [unarchive](docs/sdks/semanticsearch/README.md#unarchive) - Unarchive search

### [SmtpConfiguration](docs/sdks/smtpconfiguration/README.md)

* [get_config](docs/sdks/smtpconfiguration/README.md#get_config) - Get SMTP configuration

### [SmtpConfigurations](docs/sdks/smtpconfigurations/README.md)

* [create_or_update](docs/sdks/smtpconfigurations/README.md#create_or_update) - Create or update SMTP configuration

### [StorageConfiguration](docs/sdks/storageconfiguration/README.md)

* [create_local](docs/sdks/storageconfiguration/README.md#create_local) - Configure Local Storage
* [create_s3](docs/sdks/storageconfiguration/README.md#create_s3) - Configure AWS S3 Storage
* [create_azure_blob_config](docs/sdks/storageconfiguration/README.md#create_azure_blob_config) - Configure Azure Blob Storage
* [get](docs/sdks/storageconfiguration/README.md#get) - Get current storage configuration

### [Teams](docs/sdks/teams/README.md)

* [create](docs/sdks/teams/README.md#create) - Create a team
* [list](docs/sdks/teams/README.md#list) - List teams
* [get_by_id](docs/sdks/teams/README.md#get_by_id) - Get team by ID
* [update](docs/sdks/teams/README.md#update) - Update team
* [delete](docs/sdks/teams/README.md#delete) - Delete team
* [get_members](docs/sdks/teams/README.md#get_members) - Get team members
* [add_users](docs/sdks/teams/README.md#add_users) - Add users to team
* [remove_users](docs/sdks/teams/README.md#remove_users) - Remove users from team
* [update_user_permissions](docs/sdks/teams/README.md#update_user_permissions) - Update user role in team
* [get_user](docs/sdks/teams/README.md#get_user) - Get current user's teams
* [list_created](docs/sdks/teams/README.md#list_created) - Get teams created by current user

### [Upload](docs/sdks/upload/README.md)

* [to_knowledge_base](docs/sdks/upload/README.md#to_knowledge_base) - Upload files to knowledge base
* [records_to_folder](docs/sdks/upload/README.md#records_to_folder) - Upload files to folder

### [Uploads](docs/sdks/uploads/README.md)

* [get_limits](docs/sdks/uploads/README.md#get_limits) - Get upload limits

### [UserAccount](docs/sdks/useraccount/README.md)

* [init_auth](docs/sdks/useraccount/README.md#init_auth) - Initialize authentication session
* [authenticate](docs/sdks/useraccount/README.md#authenticate) - Authenticate user with credentials
* [generate_otp](docs/sdks/useraccount/README.md#generate_otp) - Generate and send OTP for login
* [reset_password](docs/sdks/useraccount/README.md#reset_password) - Reset password (authenticated user)
* [forgot_password](docs/sdks/useraccount/README.md#forgot_password) - Request password reset email
* [reset_password_token](docs/sdks/useraccount/README.md#reset_password_token) - Reset password with email token
* [check_password_set](docs/sdks/useraccount/README.md#check_password_set) - Check if user has password set (Internal)
* [refresh](docs/sdks/useraccount/README.md#refresh) - Refresh access token
* [logout](docs/sdks/useraccount/README.md#logout) - Logout current session

### [UserGroups](docs/sdks/usergroups/README.md)

* [create](docs/sdks/usergroups/README.md#create) - Create user group
* [list](docs/sdks/usergroups/README.md#list) - Get all user groups
* [get_by_id](docs/sdks/usergroups/README.md#get_by_id) - Get user group by ID
* [update](docs/sdks/usergroups/README.md#update) - Update user group
* [delete](docs/sdks/usergroups/README.md#delete) - Delete user group
* [add_users](docs/sdks/usergroups/README.md#add_users) - Add users to group
* [remove_users](docs/sdks/usergroups/README.md#remove_users) - Remove users from group
* [list_users](docs/sdks/usergroups/README.md#list_users) - Get users in a group
* [get_for_user](docs/sdks/usergroups/README.md#get_for_user) - Get groups for a user
* [get_stats](docs/sdks/usergroups/README.md#get_stats) - Get user group statistics

### [Users](docs/sdks/users/README.md)

* [get_all](docs/sdks/users/README.md#get_all) - Get all users
* [create](docs/sdks/users/README.md#create) - Create a new user
* [get_by_id](docs/sdks/users/README.md#get_by_id) - Get user by ID
* [update](docs/sdks/users/README.md#update) - Update user
* [delete](docs/sdks/users/README.md#delete) - Delete user
* [get_all_with_groups](docs/sdks/users/README.md#get_all_with_groups) - Get all users with their groups
* [get_email](docs/sdks/users/README.md#get_email) - Get user email by ID
* [get_by_ids](docs/sdks/users/README.md#get_by_ids) - Get users by IDs (bulk)
* [exists_by_email](docs/sdks/users/README.md#exists_by_email) - Check if user exists by email
* [get_internal](docs/sdks/users/README.md#get_internal) - Get user (internal service-to-service)
* [update_full_name](docs/sdks/users/README.md#update_full_name) - Update user full name
* [update_first_name](docs/sdks/users/README.md#update_first_name) - Update user first name
* [update_last_name](docs/sdks/users/README.md#update_last_name) - Update user last name
* [update_designation](docs/sdks/users/README.md#update_designation) - Update user designation
* [check_admin_status](docs/sdks/users/README.md#check_admin_status) - Check if user is admin
* [upload_display_picture](docs/sdks/users/README.md#upload_display_picture) - Upload display picture
* [get_display_picture](docs/sdks/users/README.md#get_display_picture) - Get display picture
* [remove_display_picture](docs/sdks/users/README.md#remove_display_picture) - Remove display picture
* [bulk_invite](docs/sdks/users/README.md#bulk_invite) - Bulk invite users
* [resend_invite](docs/sdks/users/README.md#resend_invite) - Resend user invite
* [list_with_graph](docs/sdks/users/README.md#list_with_graph) - List users (paginated with graph data)
* [get_teams](docs/sdks/users/README.md#get_teams) - Get current user's teams

### [VersionControl](docs/sdks/versioncontrol/README.md)

* [upload_next_version](docs/sdks/versioncontrol/README.md#upload_next_version) - Upload next version
* [rollback](docs/sdks/versioncontrol/README.md#rollback) - Rollback to previous version
* [check_document_modified](docs/sdks/versioncontrol/README.md#check_document_modified) - Check if document is modified

### [Webhooks](docs/sdks/webhooks/README.md)

* [verify_gmail](docs/sdks/webhooks/README.md#verify_gmail) - [Connector Service] Gmail webhook verification
* [gmail](docs/sdks/webhooks/README.md#gmail) - [Connector Service] Gmail webhook
* [admin](docs/sdks/webhooks/README.md#admin) - [Connector Service] Google Workspace Admin webhook

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.conversations.create_with_streaming(query="What are the key findings from our Q4 financial report?", record_ids=[
        "507f1f77bcf86cd799439011",
        "507f1f77bcf86cd799439012",
    ], model_key="gpt-4-turbo", model_name="GPT-4 Turbo", chat_mode="balanced")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
import os
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
    bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
) as p_client:

    res = p_client.users.upload_display_picture(file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    })

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from pipeshub import Pipeshub
from pipeshub.utils import BackoffStrategy, RetryConfig


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.user_account.init_auth(email="user@example.com",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from pipeshub import Pipeshub
from pipeshub.utils import BackoffStrategy, RetryConfig


with Pipeshub(
    server_url="https://api.example.com",
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as p_client:

    res = p_client.user_account.init_auth(email="user@example.com")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`PipeshubError`](./src/pipeshub/errors/pipeshuberror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from pipeshub import Pipeshub, errors


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:
    res = None
    try:

        res = p_client.user_account.init_auth(email="user@example.com")

        # Handle response
        print(res)


    except errors.PipeshubError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.AuthError):
            print(e.data.error)  # Optional[str]
            print(e.data.message)  # Optional[str]
            print(e.data.code)  # Optional[str]
            print(e.data.status_code)  # Optional[int]
```

### Error Classes
**Primary error:**
* [`PipeshubError`](./src/pipeshub/errors/pipeshuberror.py): The base class for HTTP error responses.

<details><summary>Less common errors (12)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`PipeshubError`](./src/pipeshub/errors/pipeshuberror.py)**:
* [`AuthError`](./src/pipeshub/errors/autherror.py): Authentication error response with details for debugging and user feedback.<br><br> <b>Common Error Codes:</b><br> <ul> <li><code>INVALID_CREDENTIALS</code> - Wrong password or OTP</li> <li><code>ACCOUNT_BLOCKED</code> - Account locked after 5 failed attempts</li> <li><code>SESSION_EXPIRED</code> - Session token has expired</li> <li><code>OTP_EXPIRED</code> - OTP code has expired (10 min validity)</li> <li><code>USER_NOT_FOUND</code> - Email not registered</li> <li><code>INVALID_TOKEN</code> - JWT token is invalid or malformed</li> <li><code>METHOD_NOT_ALLOWED</code> - Auth method not enabled for org</li> </ul>. Applicable to 10 of 286 methods.*
* [`OAuthErrorResponse`](./src/pipeshub/errors/oautherrorresponse.py): OAuth 2.0 Error Response (RFC 6749 Section 5.2). Standard error format for OAuth endpoints. Applicable to 5 of 286 methods.*
* [`BadRequestError`](./src/pipeshub/errors/badrequesterror.py): Bad request. Possible reasons:<br> <ul> <li>SMTP not configured properly (missing host, port, or fromEmail)</li> <li>Invalid or unknown email template type</li> <li>Missing required templateData fields for the selected template</li> <li>Invalid email format in sendEmailTo or sendCcTo</li> </ul>. Status code `400`. Applicable to 1 of 286 methods.*
* [`NotFoundError`](./src/pipeshub/errors/notfounderror.py): SMTP configuration not found in application config. Status code `404`. Applicable to 1 of 286 methods.*
* [`SendEmailInternalServerError`](./src/pipeshub/errors/sendemailinternalservererror.py): Internal server error. Email sending failed due to:<br> <ul> <li>SMTP server connection failure</li> <li>Authentication failure with SMTP server</li> <li>Template compilation error</li> <li>Network issues</li> </ul>. Status code `500`. Applicable to 1 of 286 methods.*
* [`FailError`](./src/pipeshub/errors/failerror.py): Service is unhealthy or dependency check failed. Status code `500`. Applicable to 1 of 286 methods.*
* [`QueryServiceHealthCheckInternalServerError`](./src/pipeshub/errors/queryservicehealthcheckinternalservererror.py): Model health check failed. Status code `500`. Applicable to 1 of 286 methods.*
* [`ResponseValidationError`](./src/pipeshub/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from pipeshub import Pipeshub
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Pipeshub(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from pipeshub import Pipeshub
from pipeshub.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Pipeshub(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Pipeshub` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from pipeshub import Pipeshub
def main():

    with Pipeshub(
        server_url="https://api.example.com",
    ) as p_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Pipeshub(
        server_url="https://api.example.com",
    ) as p_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from pipeshub import Pipeshub
import logging

logging.basicConfig(level=logging.DEBUG)
s = Pipeshub(server_url="https://example.com", debug_logger=logging.getLogger("pipeshub"))
```

You can also enable a default debug logger by setting an environment variable `PIPESHUB_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
