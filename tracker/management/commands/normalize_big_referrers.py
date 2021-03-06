import logging

from django.core.management import BaseCommand

from tracker.models import Tracker
from util.normalize_referrers import big_referrers

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = """Checkes the raw logs and generates final trackers based on them
    """

    def handle(self, *args, **options):
        for big_referrer in big_referrers:
            trackers = Tracker.objects.filter(referrer_url__contains=big_referrer[0])
            logger.info('Going to normalize {} referrers of {}'.format(trackers.count(), big_referrer[0]))
            trackers.update(referrer_url=big_referrer[1])
