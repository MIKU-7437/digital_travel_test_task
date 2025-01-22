

async_engine = create_async_engine(
    url=url,
    echo=echo,
    echo_pool=echo_pool,
    pool_size=pool_size,
    max_overflow=max_overflow,
)