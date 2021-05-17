import pytest

from topgg import types

d = {
    "defAvatar": "6debd47ed13483642cf09e832ed0bc1b",
    "invite": "",
    "website": "https://top.gg",
    "support": "KYZsaFb",
    "github": "https://github.com/top-gg/Luca",
    "longdesc": "Luca only works in the **Discord Bot List** server.    \nPrepend commands with the prefix `-` or "
    "`@Luca#1375`.    \n**Please refrain from using these commands in non testing channels.**\n- `botinfo "
    "@bot` Shows bot info, title redirects to site listing.\n- `bots @user`* Shows all bots of that user, "
    "includes bots in the queue.\n- `owner / -owners @bot`* Shows all owners of that bot.\n- `prefix "
    "@bot`* Shows the prefix of that bot.\n* Mobile friendly version exists. Just add `noembed` to the "
    "end of the command.\n",
    "shortdesc": "Luca is a bot for managing and informing members of the server",
    "prefix": "- or @Luca#1375",
    "lib": None,
    "clientid": "264811613708746752",
    "avatar": "7edcc4c6fbb0b23762455ca139f0e1c9",
    "id": "264811613708746752",
    "discriminator": "1375",
    "username": "Luca",
    "date": "2017-04-26T18:08:17.125Z",
    "server_count": 2,
    "guilds": ["417723229721853963", "264445053596991498"],
    "shards": [],
    "monthlyPoints": 19,
    "points": 397,
    "certifiedBot": False,
    "owners": ["129908908096487424"],
    "tags": ["Moderation", "Role Management", "Logging"],
    "donatebotguildid": "",
}


@pytest.fixture
def data_dict():
    return types.DataDict.from_dict(d)


@pytest.fixture
def bot_data():
    return types.BotData(**d)


@pytest.fixture
def widget_options():
    return types.WidgetOptions(id=int(d["id"]))


def test_data_dict_fields(data_dict: types.DataDict):
    for attr in data_dict:
        if "id" in attr.lower():
            assert isinstance(data_dict[attr], int) or data_dict[attr] is None
        assert data_dict.get(attr) == data_dict[attr] == getattr(data_dict, attr)


def test_bot_data_fields(bot_data: types.BotData):
    bot_data.github = "I'm a GitHub link!"
    bot_data.support = "Support has arrived!"

    for attr in bot_data:
        if "id" in attr.lower():
            assert isinstance(bot_data[attr], int) or bot_data[attr] is None
        elif isinstance(attr, list) and attr in ("owners", "guilds"):
            for item in bot_data[attr]:
                assert isinstance(item, int)
        assert bot_data.get(attr) == bot_data[attr] == getattr(bot_data, attr)


def test_widget_options_fields(widget_options: types.WidgetOptions):
    assert widget_options["colors"] == widget_options["colours"]

    widget_options.colours = {"background": 0}
    widget_options["colours"]["text"] = 255
    assert widget_options.colours == widget_options["colors"]

    for attr in widget_options:
        if "id" in attr.lower():
            assert isinstance(widget_options[attr], int) or widget_options[attr] is None
        assert (
            widget_options.get(attr)
            == widget_options[attr]
            == widget_options[attr]
            == getattr(widget_options, attr)
        )