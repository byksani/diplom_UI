from selenium.webdriver.common.by import By


class FeedPageLocators:
    LAST_ORDER = (
        By.XPATH, '//ul[contains(@class, "OrderFeed_list")]//li[contains(@class, "OrderHistory_listItem")][1]')
    LAST_ORDER_NUMBER = (
        By.XPATH, '(//ul[contains(@class, "OrderFeed_list")]//li//p[@class="text text_type_digits-default"])[1]')
    ORDER_MODAL_WINDOW = (
        By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    ORDER_IN_PROGRESS = (
        By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[1]')

    ALL_ORDERS_COUNT = (
        By.XPATH, '//p[contains(@class, "OrderFeed_number") and preceding-sibling::p[text()="Выполнено за все время:"]]')
    TODAY_ORDERS = (
        By.XPATH, '//p[contains(@class, "OrderFeed_number") and preceding-sibling::p[text()="Выполнено за сегодня:"]]')
