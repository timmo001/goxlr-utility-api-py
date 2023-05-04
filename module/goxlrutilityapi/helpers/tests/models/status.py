"""GoXLR Utility API: Tests helpers - Status Models"""
from polyfactory import Fixture
from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture

from ....models.status import Config, Files, Mixer, Paths, Status


@register_fixture
class StatusFactory(ModelFactory[Status]):
    """Status Factory"""

    __model__ = Status

    config = Fixture(Config)
    mixers = Fixture(dict[str, Mixer])
    paths = Fixture(Paths)
    files = Fixture(Files)


def test_status() -> None:
    """Test Status"""
    model = StatusFactory.build()

    assert isinstance(model, Status)
    assert isinstance(model.config, Config)
    assert isinstance(model.mixers, dict)
    assert isinstance(model.paths, Paths)
    assert isinstance(model.files, Files)
