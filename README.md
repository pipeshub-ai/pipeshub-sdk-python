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

    res = p_client.user_account.reset_password_with_token(security=models.ResetPasswordWithTokenSecurity(
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

* [list_agent_conversations](docs/sdks/agentconversations/README.md#list_agent_conversations) - List agent conversations
* [create_agent_conversation](docs/sdks/agentconversations/README.md#create_agent_conversation) - Create agent conversation
* [stream_agent_conversation](docs/sdks/agentconversations/README.md#stream_agent_conversation) - Create agent conversation with streaming
* [get_agent_conversation](docs/sdks/agentconversations/README.md#get_agent_conversation) - Get agent conversation
* [delete_agent_conversation](docs/sdks/agentconversations/README.md#delete_agent_conversation) - Delete agent conversation
* [add_agent_message](docs/sdks/agentconversations/README.md#add_agent_message) - Add message to agent conversation
* [stream_agent_message](docs/sdks/agentconversations/README.md#stream_agent_message) - Add message with streaming
* [regenerate_agent_answer](docs/sdks/agentconversations/README.md#regenerate_agent_answer) - Regenerate agent response

### [AgentTemplates](docs/sdks/agenttemplates/README.md)

* [list_agent_templates](docs/sdks/agenttemplates/README.md#list_agent_templates) - List agent templates
* [create_agent_template](docs/sdks/agenttemplates/README.md#create_agent_template) - Create agent template
* [get_agent_template](docs/sdks/agenttemplates/README.md#get_agent_template) - Get agent template
* [update_agent_template](docs/sdks/agenttemplates/README.md#update_agent_template) - Update agent template
* [delete_agent_template](docs/sdks/agenttemplates/README.md#delete_agent_template) - Delete agent template

### [Agents](docs/sdks/agents/README.md)

* [list_agents](docs/sdks/agents/README.md#list_agents) - List agents
* [create_agent](docs/sdks/agents/README.md#create_agent) - Create agent
* [list_agent_tools](docs/sdks/agents/README.md#list_agent_tools) - List available tools
* [get_agent](docs/sdks/agents/README.md#get_agent) - Get agent
* [update_agent](docs/sdks/agents/README.md#update_agent) - Update agent
* [delete_agent](docs/sdks/agents/README.md#delete_agent) - Delete agent
* [get_agent_permissions](docs/sdks/agents/README.md#get_agent_permissions) - Get agent permissions
* [update_agent_permissions](docs/sdks/agents/README.md#update_agent_permissions) - Update agent permissions
* [share_agent](docs/sdks/agents/README.md#share_agent) - Share agent

### [AIModelsProviders](docs/sdks/aimodelsproviders/README.md)

* [get_models_by_type](docs/sdks/aimodelsproviders/README.md#get_models_by_type) - Get models by type
* [get_available_models_by_type](docs/sdks/aimodelsproviders/README.md#get_available_models_by_type) - Get available models for selection
* [add_ai_model_provider](docs/sdks/aimodelsproviders/README.md#add_ai_model_provider) - Add new AI model provider
* [update_ai_model_provider](docs/sdks/aimodelsproviders/README.md#update_ai_model_provider) - Update AI model provider
* [delete_ai_model_provider](docs/sdks/aimodelsproviders/README.md#delete_ai_model_provider) - Delete AI model provider
* [set_default_ai_model](docs/sdks/aimodelsproviders/README.md#set_default_ai_model) - Set default AI model

### [AuthenticationConfiguration](docs/sdks/authenticationconfiguration/README.md)

* [set_azure_ad_auth_config](docs/sdks/authenticationconfiguration/README.md#set_azure_ad_auth_config) - Configure Azure AD authentication
* [get_azure_ad_auth_config](docs/sdks/authenticationconfiguration/README.md#get_azure_ad_auth_config) - Get Azure AD configuration
* [set_microsoft_auth_config](docs/sdks/authenticationconfiguration/README.md#set_microsoft_auth_config) - Configure Microsoft authentication
* [get_microsoft_auth_config](docs/sdks/authenticationconfiguration/README.md#get_microsoft_auth_config) - Get Microsoft authentication configuration
* [set_google_auth_config](docs/sdks/authenticationconfiguration/README.md#set_google_auth_config) - Configure Google authentication
* [get_google_auth_config](docs/sdks/authenticationconfiguration/README.md#get_google_auth_config) - Get Google authentication configuration
* [set_sso_auth_config](docs/sdks/authenticationconfiguration/README.md#set_sso_auth_config) - Configure SAML SSO authentication
* [get_sso_auth_config](docs/sdks/authenticationconfiguration/README.md#get_sso_auth_config) - Get SAML SSO configuration
* [set_o_auth_config](docs/sdks/authenticationconfiguration/README.md#set_o_auth_config) - Configure generic OAuth provider
* [get_generic_o_auth_config](docs/sdks/authenticationconfiguration/README.md#get_generic_o_auth_config) - Get generic OAuth configuration

### [Connector](docs/sdks/connector/README.md)

* [reindex_record](docs/sdks/connector/README.md#reindex_record) - Reindex single record
* [reindex_record_group](docs/sdks/connector/README.md#reindex_record_group) - Reindex record group
* [resync_connector](docs/sdks/connector/README.md#resync_connector) - Resync connector
* [get_connector_stats](docs/sdks/connector/README.md#get_connector_stats) - Get connector statistics

### [ConnectorConfiguration](docs/sdks/connectorconfiguration/README.md)

* [get_connector_config](docs/sdks/connectorconfiguration/README.md#get_connector_config) - Get connector configuration
* [update_connector_config](docs/sdks/connectorconfiguration/README.md#update_connector_config) - Update connector configuration
* [update_connector_auth_config](docs/sdks/connectorconfiguration/README.md#update_connector_auth_config) - Update authentication configuration
* [update_connector_filters_sync_config](docs/sdks/connectorconfiguration/README.md#update_connector_filters_sync_config) - Update filters and sync configuration

### [ConnectorControl](docs/sdks/connectorcontrol/README.md)

* [toggle_connector](docs/sdks/connectorcontrol/README.md#toggle_connector) - Toggle connector sync or agent

### [ConnectorFilters](docs/sdks/connectorfilters/README.md)

* [get_connector_filters](docs/sdks/connectorfilters/README.md#get_connector_filters) - Get filter options
* [save_connector_filters](docs/sdks/connectorfilters/README.md#save_connector_filters) - Save filter selections
* [get_filter_field_options](docs/sdks/connectorfilters/README.md#get_filter_field_options) - Get dynamic filter options

### [ConnectorInstances](docs/sdks/connectorinstances/README.md)

* [list_connector_instances](docs/sdks/connectorinstances/README.md#list_connector_instances) - List connector instances
* [create_connector_instance](docs/sdks/connectorinstances/README.md#create_connector_instance) - Create connector instance
* [list_active_connectors](docs/sdks/connectorinstances/README.md#list_active_connectors) - List active connector instances
* [list_inactive_connectors](docs/sdks/connectorinstances/README.md#list_inactive_connectors) - List inactive connector instances
* [list_configured_connectors](docs/sdks/connectorinstances/README.md#list_configured_connectors) - List configured connector instances
* [list_active_agent_connectors](docs/sdks/connectorinstances/README.md#list_active_agent_connectors) - List active agent connectors
* [get_connector_instance](docs/sdks/connectorinstances/README.md#get_connector_instance) - Get connector instance
* [delete_connector_instance](docs/sdks/connectorinstances/README.md#delete_connector_instance) - Delete connector instance
* [update_connector_name](docs/sdks/connectorinstances/README.md#update_connector_name) - Update connector instance name

### [ConnectorOAuth](docs/sdks/connectoroauth/README.md)

* [get_o_auth_authorization_url](docs/sdks/connectoroauth/README.md#get_o_auth_authorization_url) - Get OAuth authorization URL
* [handle_o_auth_callback](docs/sdks/connectoroauth/README.md#handle_o_auth_callback) - OAuth callback handler

### [ConnectorRegistry](docs/sdks/connectorregistry/README.md)

* [get_connector_registry](docs/sdks/connectorregistry/README.md#get_connector_registry) - List available connector types
* [get_connector_schema](docs/sdks/connectorregistry/README.md#get_connector_schema) - Get connector configuration schema

### [Conversations](docs/sdks/conversations/README.md)

* [create_conversation](docs/sdks/conversations/README.md#create_conversation) - Create a new AI conversation
* [stream_chat](docs/sdks/conversations/README.md#stream_chat) - Create conversation with streaming response
* [get_all_conversations](docs/sdks/conversations/README.md#get_all_conversations) - List all conversations
* [get_archived_conversations](docs/sdks/conversations/README.md#get_archived_conversations) - List archived conversations
* [get_conversation_by_id](docs/sdks/conversations/README.md#get_conversation_by_id) - Get conversation by ID
* [delete_conversation_by_id](docs/sdks/conversations/README.md#delete_conversation_by_id) - Delete conversation
* [add_message](docs/sdks/conversations/README.md#add_message) - Add message to conversation
* [add_message_stream](docs/sdks/conversations/README.md#add_message_stream) - Add message with streaming response
* [share_conversation](docs/sdks/conversations/README.md#share_conversation) - Share conversation with users
* [update_conversation_title](docs/sdks/conversations/README.md#update_conversation_title) - Update conversation title
* [archive_conversation](docs/sdks/conversations/README.md#archive_conversation) - Archive conversation
* [unarchive_conversation](docs/sdks/conversations/README.md#unarchive_conversation) - Unarchive conversation
* [regenerate_answer](docs/sdks/conversations/README.md#regenerate_answer) - Regenerate AI response
* [update_message_feedback](docs/sdks/conversations/README.md#update_message_feedback) - Submit feedback on AI response

### [CrawlingJobs](docs/sdks/crawlingjobs/README.md)

* [schedule_crawling_job](docs/sdks/crawlingjobs/README.md#schedule_crawling_job) - Schedule a crawling job
* [get_crawling_job_status](docs/sdks/crawlingjobs/README.md#get_crawling_job_status) - Get crawling job status
* [remove_crawling_job](docs/sdks/crawlingjobs/README.md#remove_crawling_job) - Remove a crawling job

### [DocumentManagement](docs/sdks/documentmanagement/README.md)

* [download_document](docs/sdks/documentmanagement/README.md#download_document) - Download document

### [Folders](docs/sdks/folders/README.md)

* [create_root_folder](docs/sdks/folders/README.md#create_root_folder) - Create root folder
* [get_folder_contents](docs/sdks/folders/README.md#get_folder_contents) - Get folder contents
* [update_folder](docs/sdks/folders/README.md#update_folder) - Update folder
* [delete_folder](docs/sdks/folders/README.md#delete_folder) - Delete folder
* [get_folder_children](docs/sdks/folders/README.md#get_folder_children) - Get folder children (alias for folder contents)
* [create_subfolder](docs/sdks/folders/README.md#create_subfolder) - Create subfolder

### [KnowledgeBases](docs/sdks/knowledgebases/README.md)

* [create_knowledge_base](docs/sdks/knowledgebases/README.md#create_knowledge_base) - Create a new knowledge base
* [list_knowledge_bases](docs/sdks/knowledgebases/README.md#list_knowledge_bases) - List all knowledge bases
* [get_knowledge_base](docs/sdks/knowledgebases/README.md#get_knowledge_base) - Get knowledge base by ID
* [update_knowledge_base](docs/sdks/knowledgebases/README.md#update_knowledge_base) - Update knowledge base
* [delete_knowledge_base](docs/sdks/knowledgebases/README.md#delete_knowledge_base) - Delete knowledge base
* [get_knowledge_hub_root_nodes](docs/sdks/knowledgebases/README.md#get_knowledge_hub_root_nodes) - Get knowledge hub root nodes
* [get_knowledge_hub_child_nodes](docs/sdks/knowledgebases/README.md#get_knowledge_hub_child_nodes) - Get knowledge hub child nodes

### [MetricsCollection](docs/sdks/metricscollection/README.md)

* [get_metrics_collection](docs/sdks/metricscollection/README.md#get_metrics_collection) - Get metrics collection configuration
* [toggle_metrics_collection](docs/sdks/metricscollection/README.md#toggle_metrics_collection) - Enable or disable metrics collection

### [OAuth](docs/sdks/oauthsdk/README.md)

* [exchange_o_auth_code](docs/sdks/oauthsdk/README.md#exchange_o_auth_code) - Exchange OAuth authorization code for tokens

### [OAuthApps](docs/sdks/oauthapps/README.md)

* [list_o_auth_apps](docs/sdks/oauthapps/README.md#list_o_auth_apps) - List OAuth apps
* [create_o_auth_app](docs/sdks/oauthapps/README.md#create_o_auth_app) - Create OAuth app
* [list_o_auth_scopes](docs/sdks/oauthapps/README.md#list_o_auth_scopes) - List available scopes
* [get_o_auth_app](docs/sdks/oauthapps/README.md#get_o_auth_app) - Get OAuth app details
* [update_o_auth_app](docs/sdks/oauthapps/README.md#update_o_auth_app) - Update OAuth app
* [delete_o_auth_app](docs/sdks/oauthapps/README.md#delete_o_auth_app) - Delete OAuth app
* [regenerate_o_auth_app_secret](docs/sdks/oauthapps/README.md#regenerate_o_auth_app_secret) - Regenerate client secret
* [suspend_o_auth_app](docs/sdks/oauthapps/README.md#suspend_o_auth_app) - Suspend OAuth app
* [activate_o_auth_app](docs/sdks/oauthapps/README.md#activate_o_auth_app) - Activate suspended OAuth app
* [list_o_auth_app_tokens](docs/sdks/oauthapps/README.md#list_o_auth_app_tokens) - List app tokens
* [revoke_all_o_auth_app_tokens](docs/sdks/oauthapps/README.md#revoke_all_o_auth_app_tokens) - Revoke all app tokens

### [OAuthConfiguration](docs/sdks/oauthconfiguration/README.md)

* [get_o_auth_registry](docs/sdks/oauthconfiguration/README.md#get_o_auth_registry) - List OAuth-capable connector types
* [get_o_auth_connector_type](docs/sdks/oauthconfiguration/README.md#get_o_auth_connector_type) - Get OAuth connector type details
* [list_o_auth_configs](docs/sdks/oauthconfiguration/README.md#list_o_auth_configs) - List OAuth configurations
* [list_o_auth_configs_by_type](docs/sdks/oauthconfiguration/README.md#list_o_auth_configs_by_type) - List OAuth configs for connector type
* [create_o_auth_config](docs/sdks/oauthconfiguration/README.md#create_o_auth_config) - Create OAuth configuration
* [get_o_auth_config](docs/sdks/oauthconfiguration/README.md#get_o_auth_config) - Get OAuth configuration
* [update_o_auth_config](docs/sdks/oauthconfiguration/README.md#update_o_auth_config) - Update OAuth configuration
* [delete_o_auth_config](docs/sdks/oauthconfiguration/README.md#delete_o_auth_config) - Delete OAuth configuration

### [OAuthProvider](docs/sdks/oauthprovider/README.md)

* [oauth_authorize](docs/sdks/oauthprovider/README.md#oauth_authorize) - Initiate OAuth authorization flow
* [oauth_authorize_consent](docs/sdks/oauthprovider/README.md#oauth_authorize_consent) - Submit authorization consent
* [oauth_token](docs/sdks/oauthprovider/README.md#oauth_token) - Exchange authorization code for tokens
* [oauth_revoke](docs/sdks/oauthprovider/README.md#oauth_revoke) - Revoke an access or refresh token
* [oauth_introspect](docs/sdks/oauthprovider/README.md#oauth_introspect) - Introspect a token

### [OpenIDConnect](docs/sdks/openidconnect/README.md)

* [oauth_user_info](docs/sdks/openidconnect/README.md#oauth_user_info) - Get authenticated user information
* [openid_configuration](docs/sdks/openidconnect/README.md#openid_configuration) - OpenID Connect Discovery
* [jwks](docs/sdks/openidconnect/README.md#jwks) - JSON Web Key Set

### [OrganizationAuthConfig](docs/sdks/organizationauthconfig/README.md)

* [get_auth_methods](docs/sdks/organizationauthconfig/README.md#get_auth_methods) - Get organization authentication methods
* [update_auth_method](docs/sdks/organizationauthconfig/README.md#update_auth_method) - Update organization authentication methods

### [Organizations](docs/sdks/organizations/README.md)

* [check_org_exists](docs/sdks/organizations/README.md#check_org_exists) - Check if organization exists
* [create_organization](docs/sdks/organizations/README.md#create_organization) - Create organization
* [get_current_organization](docs/sdks/organizations/README.md#get_current_organization) - Get current organization
* [update_organization](docs/sdks/organizations/README.md#update_organization) - Update organization
* [delete_organization](docs/sdks/organizations/README.md#delete_organization) - Delete organization
* [upload_organization_logo](docs/sdks/organizations/README.md#upload_organization_logo) - Upload organization logo
* [get_organization_logo](docs/sdks/organizations/README.md#get_organization_logo) - Get organization logo
* [delete_organization_logo](docs/sdks/organizations/README.md#delete_organization_logo) - Delete organization logo
* [get_onboarding_status](docs/sdks/organizations/README.md#get_onboarding_status) - Get onboarding status
* [update_onboarding_status](docs/sdks/organizations/README.md#update_onboarding_status) - Update onboarding status

### [Permissions](docs/sdks/permissions/README.md)

* [create_kb_permission](docs/sdks/permissions/README.md#create_kb_permission) - Grant permissions
* [list_kb_permissions](docs/sdks/permissions/README.md#list_kb_permissions) - List permissions
* [update_kb_permissions](docs/sdks/permissions/README.md#update_kb_permissions) - Update permissions
* [delete_kb_permissions](docs/sdks/permissions/README.md#delete_kb_permissions) - Remove permissions

### [PlatformSettings](docs/sdks/platformsettingssdk/README.md)

* [set_platform_settings](docs/sdks/platformsettingssdk/README.md#set_platform_settings) - Update platform settings
* [get_platform_settings](docs/sdks/platformsettingssdk/README.md#get_platform_settings) - Get platform settings
* [get_available_feature_flags](docs/sdks/platformsettingssdk/README.md#get_available_feature_flags) - Get available feature flags
* [set_custom_system_prompt](docs/sdks/platformsettingssdk/README.md#set_custom_system_prompt) - Update custom system prompt
* [get_custom_system_prompt](docs/sdks/platformsettingssdk/README.md#get_custom_system_prompt) - Get custom system prompt

### [PublicURLs](docs/sdks/publicurls/README.md)

* [set_frontend_public_url](docs/sdks/publicurls/README.md#set_frontend_public_url) - Set frontend public URL
* [get_frontend_public_url](docs/sdks/publicurls/README.md#get_frontend_public_url) - Get frontend public URL
* [set_connector_public_url](docs/sdks/publicurls/README.md#set_connector_public_url) - Set connector public URL
* [get_connector_public_url](docs/sdks/publicurls/README.md#get_connector_public_url) - Get connector public URL

### [Records](docs/sdks/records/README.md)

* [get_all_records](docs/sdks/records/README.md#get_all_records) - Get all records across knowledge bases
* [get_kb_records](docs/sdks/records/README.md#get_kb_records) - Get records for a knowledge base
* [get_kb_children](docs/sdks/records/README.md#get_kb_children) - Get KB children (alias for records)
* [get_record_by_id](docs/sdks/records/README.md#get_record_by_id) - Get record by ID
* [update_record](docs/sdks/records/README.md#update_record) - Update record
* [delete_record](docs/sdks/records/README.md#delete_record) - Delete record
* [stream_record_buffer](docs/sdks/records/README.md#stream_record_buffer) - Stream record content

### [Saml](docs/sdks/saml/README.md)

* [sign_in_via_saml](docs/sdks/saml/README.md#sign_in_via_saml) - Initiate SAML sign-in flow

### [SemanticSearch](docs/sdks/semanticsearch/README.md)

* [search](docs/sdks/semanticsearch/README.md#search) - Perform semantic search
* [search_history](docs/sdks/semanticsearch/README.md#search_history) - Get search history
* [delete_all_search_history](docs/sdks/semanticsearch/README.md#delete_all_search_history) - Clear all search history

### [SMTPConfiguration](docs/sdks/smtpconfiguration/README.md)

* [create_smtp_config](docs/sdks/smtpconfiguration/README.md#create_smtp_config) - Create or update SMTP configuration
* [get_smtp_config](docs/sdks/smtpconfiguration/README.md#get_smtp_config) - Get SMTP configuration

### [StorageConfiguration](docs/sdks/storageconfiguration/README.md)

* [get_storage_config](docs/sdks/storageconfiguration/README.md#get_storage_config) - Get current storage configuration

### [Teams](docs/sdks/teams/README.md)

* [create_team](docs/sdks/teams/README.md#create_team) - Create a team
* [list_teams](docs/sdks/teams/README.md#list_teams) - List teams
* [get_team_by_id](docs/sdks/teams/README.md#get_team_by_id) - Get team by ID
* [update_team](docs/sdks/teams/README.md#update_team) - Update team
* [delete_team](docs/sdks/teams/README.md#delete_team) - Delete team
* [get_user_teams](docs/sdks/teams/README.md#get_user_teams) - Get current user's teams

### [ToolsetConfiguration](docs/sdks/toolsetconfiguration/README.md)

* [get_toolset_config](docs/sdks/toolsetconfiguration/README.md#get_toolset_config) - Get toolset configuration
* [~~save_toolset_config~~](docs/sdks/toolsetconfiguration/README.md#save_toolset_config) - Save toolset configuration :warning: **Deprecated**
* [update_toolset_config](docs/sdks/toolsetconfiguration/README.md#update_toolset_config) - Update toolset configuration
* [delete_toolset_config](docs/sdks/toolsetconfiguration/README.md#delete_toolset_config) - Delete toolset configuration

### [ToolsetInstances](docs/sdks/toolsetinstances/README.md)

* [create_toolset](docs/sdks/toolsetinstances/README.md#create_toolset) - Create toolset instance
* [list_configured_toolsets](docs/sdks/toolsetinstances/README.md#list_configured_toolsets) - List configured toolsets
* [check_toolset_status](docs/sdks/toolsetinstances/README.md#check_toolset_status) - Check toolset status

### [ToolsetOAuth](docs/sdks/toolsetoauth/README.md)

* [get_toolset_o_auth_url](docs/sdks/toolsetoauth/README.md#get_toolset_o_auth_url) - Get OAuth authorization URL
* [handle_toolset_o_auth_callback](docs/sdks/toolsetoauth/README.md#handle_toolset_o_auth_callback) - Handle OAuth callback

### [ToolsetRegistry](docs/sdks/toolsetregistry/README.md)

* [list_toolset_registry](docs/sdks/toolsetregistry/README.md#list_toolset_registry) - List available toolsets
* [get_toolset_schema](docs/sdks/toolsetregistry/README.md#get_toolset_schema) - Get toolset schema

### [Upload](docs/sdks/upload/README.md)

* [upload_records_to_kb](docs/sdks/upload/README.md#upload_records_to_kb) - Upload files to knowledge base
* [upload_records_to_folder](docs/sdks/upload/README.md#upload_records_to_folder) - Upload files to folder
* [get_upload_limits](docs/sdks/upload/README.md#get_upload_limits) - Get upload limits

### [UserAccount](docs/sdks/useraccount/README.md)

* [init_auth](docs/sdks/useraccount/README.md#init_auth) - Initialize authentication session
* [authenticate](docs/sdks/useraccount/README.md#authenticate) - Authenticate user with credentials
* [generate_login_otp](docs/sdks/useraccount/README.md#generate_login_otp) - Generate and send OTP for login
* [forgot_password](docs/sdks/useraccount/README.md#forgot_password) - Request password reset email
* [reset_password_with_token](docs/sdks/useraccount/README.md#reset_password_with_token) - Reset password with email token
* [refresh_token](docs/sdks/useraccount/README.md#refresh_token) - Refresh access token
* [logout](docs/sdks/useraccount/README.md#logout) - Logout current session

### [UserGroups](docs/sdks/usergroups/README.md)

* [create_user_group](docs/sdks/usergroups/README.md#create_user_group) - Create user group
* [get_all_user_groups](docs/sdks/usergroups/README.md#get_all_user_groups) - Get all user groups
* [get_user_group_by_id](docs/sdks/usergroups/README.md#get_user_group_by_id) - Get user group by ID
* [update_user_group](docs/sdks/usergroups/README.md#update_user_group) - Update user group
* [delete_user_group](docs/sdks/usergroups/README.md#delete_user_group) - Delete user group
* [add_users_to_group](docs/sdks/usergroups/README.md#add_users_to_group) - Add users to group
* [remove_users_from_group](docs/sdks/usergroups/README.md#remove_users_from_group) - Remove users from group
* [get_groups_for_user](docs/sdks/usergroups/README.md#get_groups_for_user) - Get groups for a user

### [Users](docs/sdks/users/README.md)

* [get_all_users](docs/sdks/users/README.md#get_all_users) - Get all users
* [create_user](docs/sdks/users/README.md#create_user) - Create a new user
* [get_user_by_id](docs/sdks/users/README.md#get_user_by_id) - Get user by ID
* [update_user](docs/sdks/users/README.md#update_user) - Update user
* [delete_user](docs/sdks/users/README.md#delete_user) - Delete user
* [get_user_email_by_id](docs/sdks/users/README.md#get_user_email_by_id) - Get user email by ID
* [upload_user_display_picture](docs/sdks/users/README.md#upload_user_display_picture) - Upload display picture
* [get_user_display_picture](docs/sdks/users/README.md#get_user_display_picture) - Get display picture
* [remove_user_display_picture](docs/sdks/users/README.md#remove_user_display_picture) - Remove display picture
* [bulk_invite_users](docs/sdks/users/README.md#bulk_invite_users) - Bulk invite users
* [resend_user_invite](docs/sdks/users/README.md#resend_user_invite) - Resend user invite
* [list_users_graph](docs/sdks/users/README.md#list_users_graph) - List users (paginated with graph data)
* [unblock_user](docs/sdks/users/README.md#unblock_user) - Unblock a user in organization

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
from pipeshub import Pipeshub, models


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.conversations.stream_chat(security=models.StreamChatSecurity(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ), query="What are the key findings from our Q4 financial report?", record_ids=[
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

    res = p_client.users.upload_user_display_picture(file={
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

<details><summary>Less common errors (7)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`PipeshubError`](./src/pipeshub/errors/pipeshuberror.py)**:
* [`AuthError`](./src/pipeshub/errors/autherror.py): Authentication error response with details for debugging and user feedback.<br><br> <b>Common Error Codes:</b><br> <ul> <li><code>INVALID_CREDENTIALS</code> - Wrong password or OTP</li> <li><code>ACCOUNT_BLOCKED</code> - Account locked after 5 failed attempts</li> <li><code>SESSION_EXPIRED</code> - Session token has expired</li> <li><code>OTP_EXPIRED</code> - OTP code has expired (10 min validity)</li> <li><code>USER_NOT_FOUND</code> - Email not registered</li> <li><code>INVALID_TOKEN</code> - JWT token is invalid or malformed</li> <li><code>METHOD_NOT_ALLOWED</code> - Auth method not enabled for org</li> </ul>. Applicable to 7 of 211 methods.*
* [`OAuthErrorResponse`](./src/pipeshub/errors/oautherrorresponse.py): OAuth 2.0 Error Response (RFC 6749 Section 5.2). Standard error format for OAuth endpoints. Applicable to 5 of 211 methods.*
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
