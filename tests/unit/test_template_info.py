# This file is part of the Valkyrja Framework package.
#
# (c) Melech Mizrachi <melechmizrachi@gmail.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from valkyrja.template.constant.template_info import TemplateInfo


def test_version_is_set() -> None:
    assert TemplateInfo.VERSION


def test_version_build_date_time_is_set() -> None:
    assert TemplateInfo.VERSION_BUILD_DATE_TIME
