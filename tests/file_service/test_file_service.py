import pytest
from mock import mock_open
from src.file_service import file_service


def test_read_file_success_flow(mocker):
    mocked_open = mock_open()
    mocker.patch('builtins.open', mocked_open, create=True)
    mocked_open().read.return_value = 'test_file_content'

    return_value = file_service.read_file('test_file_name')

    mocked_open.assert_called_with('test_file_name', 'r')
    assert return_value == 'test_file_content'


def test_read_file_error_flow(mocker):
    mocked_open = mock_open()
    mocker.patch('builtins.open', mocked_open, create=True)
    mocked_open.side_effect = OSError()

    with pytest.raises(OSError):
        file_service.read_file('test_file_name')
    mocked_open.assert_called_with('test_file_name', 'r')


def test_create_file_success_flow(mocker):
    mocked_open = mock_open()
    mocker.patch('builtins.open', mocked_open, create=True)
    mocker.patch('src.utils.utils.generate_random_string').return_value = "test_file_name"

    file_service.create_file('test_content')

    mocked_open.assert_called_with('test_file_name', 'w')
    mocked_open().write.assert_called_with('test_content')


def test_create_file_error_flow(mocker):
    mocked_open = mock_open()
    mocker.patch('builtins.open', mocked_open, create=True)
    mocked_open.side_effect = OSError()
    mocker.patch('src.utils.utils.generate_random_string').return_value = "test_file_name"

    with pytest.raises(OSError):
        file_service.create_file('test_content')
    mocked_open.assert_called_with('test_file_name', 'w')


def test_delete_file_success_flow(mocker):
    remove_mock = mocker.patch('os.remove')
    file_service.delete_file('test_file')
    remove_mock.assert_called_once()


def test_delete_file_error_flow(mocker):
    mocker.patch('os.remove', side_effect=OSError())
    with pytest.raises(OSError):
        file_service.delete_file('test_file')


def test_list_dir_success_flow(mocker):
    ls_mock = mocker.patch('os.listdir')
    ls_mock.return_value = ['abc']
    assert file_service.list_dir() == ['abc']


def test_list_dir_error_flow(mocker):
    mocker.patch('os.listdir', side_effect=OSError())
    with pytest.raises(OSError):
        file_service.list_dir()


def test_change_dir_success_flow(mocker):
    cd_mock = mocker.patch('os.chdir')
    file_service.change_dir('test_directory')
    cd_mock.assert_called_once()


def test_change_dir_error_flow(mocker):
    mocker.patch('os.chdir', side_effect=OSError())
    with pytest.raises(OSError):
        file_service.change_dir('')


def test_get_current_dir_success_flow(mocker):
    cd_mock = mocker.patch('os.getcwd')
    cd_mock.return_value = 'abc'
    assert file_service.get_current_dir() == 'abc'


def test_get_current_dir_error_flow(mocker):
    mocker.patch('os.getcwd', side_effect=OSError())
    with pytest.raises(OSError):
        file_service.get_current_dir()


def test_get_file_metadata_success_flow(mocker):
    ls_mock = mocker.patch('os.stat')
    ls_mock.return_value.st_ctime = 123
    ls_mock.return_value.st_mtime = 456
    ls_mock.return_value.st_size = 789
    assert file_service.get_file_metadata('test_file') == (123, 456, 789)


def test_get_file_metadata_error_flow(mocker):
    mocker.patch('os.stat', side_effect=OSError())
    with pytest.raises(OSError):
        file_service.get_file_metadata('')
