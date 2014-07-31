from __future__ import unicode_literals

import mock

import pytest

import spotify

from mopidy_spotify import backend


@pytest.yield_fixture
def spotify_mock():
    patcher = mock.patch.object(backend, 'spotify', spec=spotify)
    yield patcher.start()
    patcher.stop()


@pytest.fixture
def sp_user_mock():
    sp_user = mock.Mock(spec=spotify.User)
    sp_user.is_loaded = True
    sp_user.canonical_name = 'alice'
    return sp_user


@pytest.fixture
def sp_track_mock():
    sp_track = mock.Mock(spec=spotify.Track)
    sp_track.is_loaded = True
    sp_track.availability = spotify.TrackAvailability.AVAILABLE
    sp_track.link.uri = 'spotify:track:abc'
    sp_track.name = 'ABC 123'
    sp_track.duration = 174300
    sp_track.index = 7
    return sp_track


@pytest.fixture
def sp_playlist_mock(sp_user_mock, sp_track_mock):
    sp_playlist = mock.Mock(spec=spotify.Playlist)
    sp_playlist.is_loaded = True
    sp_playlist.owner = sp_user_mock
    sp_playlist.link.uri = 'spotify:playlist:alice:foo'
    sp_playlist.name = 'Foo'
    sp_playlist.tracks = [sp_track_mock]
    return sp_playlist