# This file is part of the Valkyrja Framework package.
#
# (c) Melech Mizrachi <melechmizrachi@gmail.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from typing import Final


class TemplateInfo:
    """Package version metadata, updated by the release workflow."""

    VERSION: Final[str] = "1.0.0"
    VERSION_BUILD_DATE_TIME: Final[str] = "January 1 2025 00:00:00 MST"
