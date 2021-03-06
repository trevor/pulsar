from .test_utils import (
    BaseManagerTestCase,
    skipUnlessModule
)

from pulsar.managers.queued_drmaa import DrmaaQueueManager


class DrmaaManagerTest(BaseManagerTestCase):

    def setUp(self):
        super(DrmaaManagerTest, self).setUp()
        self._set_manager()

    def tearDown(self):
        super(DrmaaManagerTest, self).setUp()
        self.manager.shutdown()

    def _set_manager(self, **kwds):
        self.manager = DrmaaQueueManager('_default_', self.app, **kwds)

    @skipUnlessModule("drmaa")
    def test_simple_execution(self):
        self._test_simple_execution(self.manager)

    @skipUnlessModule("drmaa")
    def test_cancel(self):
        self._test_cancelling(self.manager)
