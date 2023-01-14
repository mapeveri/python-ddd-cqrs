MODULES = [
    "src.shared.infrastructure.api_controller",
    "src.shared.infrastructure.bus.event.mapping",
    "src.shared.infrastructure.bus.register",
    "src.shared.infrastructure.persistence.sqlalchemy.unit_of_work._sql_alchemy_unit_of_work",
    "src.shared.infrastructure.persistence.sqlalchemy.utils.transactions",
    "src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_event_repository",
    "src.marketplace.event.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_zone_repository",
    "src.marketplace.event.infrastructure.persistence.elasticsearch.repository"
    ".elasticsearch_event_response_repository",
    "src.marketplace.event.infrastructure.services.events_provider.process_events_provider",
    "src.shared.infrastructure.persistence.sqlalchemy.repository.sqlalchemy_outbox_repository",
    "src.shared.infrastructure.console.commands.publish_domain_events_cli",
    "src.marketplace.retention.infrastructure.email.flask_send_email",
]
