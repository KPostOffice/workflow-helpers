# thoth-common
# Copyright(C) 2020 Francesco Murdaca
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Exceptions used within workflow-helpers."""


class TriggerFinishedWebhookInputsMissing(Exception):
    """An exception raised if there are inputs missing for Triggering Finished Webhook."""


class SourceDistroNotFound(Exception):
    """An exception is raised if there is no source distro found for a given package."""


class VersionDoesNotExist(Exception):
    """An exception is raised if the requested version does not exist at all."""
