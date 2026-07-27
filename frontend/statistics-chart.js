console.log("statistics-chart.js aktif");

(() => {
    const HEADER_STATISTIK =
        "STATISTIK KEJADIAN BENCANA SITABA";

    let activeChart = null;

    const SECTION_CONFIG = {
        jenis_bencana: {
            start: "Berdasarkan Jenis Bencana",
            end: "Berdasarkan Provinsi"
        },

        provinsi: {
            start: "Berdasarkan Provinsi",
            end: "Berdasarkan Kabupaten/Kota"
        },

        kabupaten_kota: {
            start: "Berdasarkan Kabupaten/Kota",
            end: "Berdasarkan Tahun"
        },

        tahun: {
            start: "Berdasarkan Tahun",
            end: "Berdasarkan Bulan"
        },

        bulan: {
            start: "Berdasarkan Bulan",
            end: "Sumber"
        }
    };


    /*
     * Menampilkan nilai angka pada chart
     * tanpa plugin eksternal.
     */
    const valueLabelPlugin = {
        id: "sitabaValueLabel",

        afterDatasetsDraw(chart) {
            const ctx = chart.ctx;

            const isHorizontal =
                chart.options.indexAxis === "y";

            ctx.save();

            ctx.font =
                "bold 11px Arial, sans-serif";

            ctx.fillStyle = "#1f2937";

            chart.data.datasets.forEach(
                (dataset, datasetIndex) => {
                    const meta =
                        chart.getDatasetMeta(
                            datasetIndex
                        );

                    if (meta.hidden) {
                        return;
                    }

                    meta.data.forEach(
                        (element, index) => {
                            const value = Number(
                                dataset.data[index]
                            );

                            if (
                                !Number.isFinite(
                                    value
                                )
                            ) {
                                return;
                            }

                            const position =
                                element.tooltipPosition();

                            if (isHorizontal) {
                                ctx.textAlign =
                                    "left";

                                ctx.textBaseline =
                                    "middle";

                                ctx.fillText(
                                    String(value),
                                    position.x + 7,
                                    position.y
                                );
                            } else {
                                ctx.textAlign =
                                    "center";

                                ctx.textBaseline =
                                    "bottom";

                                ctx.fillText(
                                    String(value),
                                    position.x,
                                    position.y - 6
                                );
                            }
                        }
                    );
                }
            );

            ctx.restore();
        }
    };


    function normalizeText(text) {
        return String(text || "")
            .replace(/\r/g, "")
            .replace(/\u00a0/g, " ")
            .trim();
    }


    function extractSection(
        fullText,
        startTitle,
        endTitle
    ) {
        const text =
            normalizeText(fullText);

        const startIndex =
            text.indexOf(startTitle);

        if (startIndex === -1) {
            return "";
        }

        const contentStart =
            startIndex +
            startTitle.length;

        const endIndex =
            text.indexOf(
                endTitle,
                contentStart
            );

        if (endIndex === -1) {
            return text.slice(
                contentStart
            );
        }

        return text.slice(
            contentStart,
            endIndex
        );
    }


    /*
     * Membaca seluruh statistik meskipun
     * isi bubble digabung menjadi satu baris.
     */
    function parseStatisticItems(
        sectionText
    ) {
        const text =
            normalizeText(sectionText);

        const items = [];

        const pattern =
            /(?:^|[•\n\r])\s*([^•\n\r:]+?)\s*:\s*([\d.,]+)\s*kejadian/gi;

        let match;

        while (
            (match =
                pattern.exec(text)) !==
            null
        ) {
            const label =
                String(match[1]).trim();

            const valueText =
                String(match[2]).trim();

            const normalizedValue =
                valueText
                    .replace(/\./g, "")
                    .replace(/,/g, "");

            const value =
                Number(normalizedValue);

            if (
                label &&
                Number.isFinite(value)
            ) {
                items.push({
                    label,
                    value
                });
            }
        }

        return items;
    }


    function buildChartData(
        fullText
    ) {
        const result = {};

        Object.entries(
            SECTION_CONFIG
        ).forEach(
            ([key, config]) => {
                const section =
                    extractSection(
                        fullText,
                        config.start,
                        config.end
                    );

                result[key] =
                    parseStatisticItems(
                        section
                    );
            }
        );

        return result;
    }


    /*
     * Mencari elemen bubble paling dalam
     * yang memuat jawaban statistik.
     */
    function findStatisticsMessageElements(
        chatBody
    ) {
        const elements =
            Array.from(
                chatBody.querySelectorAll(
                    "*"
                )
            );

        return elements.filter(
            (element) => {
                const text =
                    normalizeText(
                        element.textContent
                    );

                if (
                    !text.includes(
                        HEADER_STATISTIK
                    )
                ) {
                    return false;
                }

                const childHasHeader =
                    Array.from(
                        element.children
                    ).some(
                        (child) =>
                            normalizeText(
                                child.textContent
                            ).includes(
                                HEADER_STATISTIK
                            )
                    );

                return !childHasHeader;
            }
        );
    }


    function createOptionButton(
        label,
        items,
        chartType,
        title,
        menu
    ) {
        const button =
            document.createElement(
                "button"
            );

        button.type = "button";

        button.className =
            "statistics-chart-option";

        button.textContent = label;

        button.addEventListener(
            "click",
            () => {
                renderChart(
                    items,
                    chartType,
                    title
                );

                menu.hidden = true;
            }
        );

        return button;
    }


    function attachChartButton(
        messageElement
    ) {
        if (
            messageElement.dataset
                .statisticsChartAttached ===
            "true"
        ) {
            return;
        }

        const fullText =
            normalizeText(
                messageElement.textContent
            );

        if (
            !fullText.includes(
                HEADER_STATISTIK
            )
        ) {
            return;
        }

        const chartData =
            buildChartData(fullText);

        const availableSections =
            Object.entries(
                chartData
            ).filter(
                ([, items]) =>
                    Array.isArray(items) &&
                    items.length > 0
            );

        if (
            availableSections.length ===
            0
        ) {
            console.warn(
                "Jawaban statistik ditemukan, tetapi data chart tidak dapat dibaca."
            );

            return;
        }

        messageElement.dataset
            .statisticsChartAttached =
            "true";

        const wrapper =
            document.createElement(
                "div"
            );

        wrapper.className =
            "statistics-chart-actions";

        const mainButton =
            document.createElement(
                "button"
            );

        mainButton.type = "button";

        mainButton.className =
            "statistics-chart-main-button";

        mainButton.textContent =
            "📊 Chart";

        const menu =
            document.createElement(
                "div"
            );

        menu.className =
            "statistics-chart-menu";

        menu.hidden = true;

        const buttonConfig = [
            {
                key: "jenis_bencana",
                label: "Jenis Bencana",
                chartType: "bar",
                title:
                    "Statistik Berdasarkan Jenis Bencana"
            },
            {
                key: "provinsi",
                label: "Provinsi",
                chartType: "bar",
                title:
                    "Statistik Berdasarkan Provinsi"
            },
            {
                key: "kabupaten_kota",
                label:
                    "Kabupaten/Kota",
                chartType: "bar",
                title:
                    "Statistik Berdasarkan Kabupaten/Kota"
            },
            {
                key: "bulan",
                label:
                    "Tren Bulanan",
                chartType: "line",
                title:
                    "Tren Kejadian Bencana Per Bulan"
            },
            {
                key: "tahun",
                label: "Tahun",
                chartType: "bar",
                title:
                    "Statistik Berdasarkan Tahun"
            }
        ];

        buttonConfig.forEach(
            (config) => {
                const items =
                    chartData[config.key];

                if (
                    !Array.isArray(
                        items
                    ) ||
                    items.length === 0
                ) {
                    return;
                }

                menu.appendChild(
                    createOptionButton(
                        config.label,
                        items,
                        config.chartType,
                        config.title,
                        menu
                    )
                );
            }
        );

        mainButton.addEventListener(
            "click",
            () => {
                menu.hidden =
                    !menu.hidden;
            }
        );

        wrapper.appendChild(
            mainButton
        );

        wrapper.appendChild(menu);

        messageElement
            .insertAdjacentElement(
                "afterend",
                wrapper
            );
    }


    function removeOldChart(
        chatBody
    ) {
        const oldContainers =
            chatBody.querySelectorAll(
                ".statistics-chart-container"
            );

        oldContainers.forEach(
            (container) =>
                container.remove()
        );

        if (activeChart) {
            activeChart.destroy();
            activeChart = null;
        }
    }


    /*
     * Hanya menyembunyikan tombol
     * pertanyaan bawaan.
     *
     * Wadah #suggestedQuestions tidak
     * disembunyikan supaya chart tidak ikut
     * hilang.
     */
    function setQuickChatVisibility(
        hidden
    ) {
        const quickChatButtons =
            document.querySelectorAll(
                "#suggestedQuestions button, " +
                ".suggested-questions button, " +
                "button.quick-chat-button"
            );

        quickChatButtons.forEach(
            (button) => {
                const isChartButton =
                    button.classList.contains(
                        "statistics-chart-main-button"
                    ) ||
                    button.classList.contains(
                        "statistics-chart-option"
                    ) ||
                    button.classList.contains(
                        "statistics-chart-close"
                    );

                if (isChartButton) {
                    return;
                }

                if (hidden) {
                    if (
                        button.dataset
                            .previousDisplay ===
                        undefined
                    ) {
                        button.dataset
                            .previousDisplay =
                            button.style
                                .display || "";
                    }

                    button.style.display =
                        "none";
                } else {
                    button.style.display =
                        button.dataset
                            .previousDisplay ||
                        "";

                    delete button.dataset
                        .previousDisplay;
                }
            }
        );
    }


    function renderChart(
        items,
        chartType,
        title
    ) {
        if (
            typeof Chart ===
            "undefined"
        ) {
            console.error(
                "Chart.js belum dimuat."
            );

            alert(
                "Chart.js belum tersedia."
            );

            return;
        }

        const chatBody =
            document.getElementById(
                "chatBody"
            );

        if (!chatBody) {
            console.error(
                "Elemen #chatBody tidak ditemukan."
            );

            return;
        }

        /*
         * Hapus chart lama hanya ketika
         * pengguna memilih chart baru.
         */
        removeOldChart(chatBody);

        /*
         * Sembunyikan tombol pertanyaan
         * bawaan tanpa menyembunyikan chart.
         */
        setQuickChatVisibility(true);

        const container =
            document.createElement(
                "div"
            );

        container.className =
            "statistics-chart-container";

        const closeButton =
            document.createElement(
                "button"
            );

        closeButton.type =
            "button";

        closeButton.className =
            "statistics-chart-close";

        closeButton.textContent =
            "×";

        closeButton.title =
            "Tutup chart";

        const canvas =
            document.createElement(
                "canvas"
            );

        container.appendChild(
            closeButton
        );

        container.appendChild(
            canvas
        );

        chatBody.appendChild(
            container
        );

        closeButton.addEventListener(
            "click",
            () => {
                if (activeChart) {
                    activeChart.destroy();
                    activeChart = null;
                }

                container.remove();

                setQuickChatVisibility(
                    false
                );
            }
        );

        const horizontalBar =
            chartType === "bar" &&
            items.length >= 6;

        const labels =
            items.map(
                (item) =>
                    item.label
            );

        const values =
            items.map(
                (item) =>
                    Number(item.value)
            );

        activeChart =
            new Chart(canvas, {
                type: chartType,

                plugins: [
                    valueLabelPlugin
                ],

                data: {
                    labels,

                    datasets: [
                        {
                            label:
                                "Jumlah Kejadian",

                            data: values,

                            borderWidth:
                                2,

                            tension:
                                chartType ===
                                "line"
                                    ? 0.25
                                    : 0,

                            pointRadius:
                                chartType ===
                                "line"
                                    ? 4
                                    : 0,

                            pointHoverRadius:
                                chartType ===
                                "line"
                                    ? 6
                                    : 0
                        }
                    ]
                },

                options: {
                    responsive:
                        true,

                    maintainAspectRatio:
                        false,

                    indexAxis:
                        horizontalBar
                            ? "y"
                            : "x",

                    layout: {
                        padding: {
                            top: 28,

                            right:
                                horizontalBar
                                    ? 55
                                    : 15,

                            bottom: 10,

                            left: 5
                        }
                    },

                    plugins: {
                        title: {
                            display:
                                true,

                            text: title,

                            padding: {
                                top: 4,
                                bottom: 20
                            },

                            font: {
                                size: 14,
                                weight:
                                    "bold"
                            }
                        },

                        legend: {
                            display:
                                chartType ===
                                "line"
                        },

                        tooltip: {
                            callbacks: {
                                label(
                                    context
                                ) {
                                    return (
                                        `${context.raw} ` +
                                        "kejadian"
                                    );
                                }
                            }
                        }
                    },

                    scales: {
                        x: {
                            beginAtZero:
                                true,

                            ticks: {
                                precision:
                                    0,

                                autoSkip:
                                    false,

                                maxRotation:
                                    horizontalBar
                                        ? 0
                                        : 45,

                                minRotation:
                                    0
                            },

                            grid: {
                                display:
                                    true
                            }
                        },

                        y: {
                            beginAtZero:
                                true,

                            ticks: {
                                precision:
                                    0,

                                autoSkip:
                                    false
                            },

                            grid: {
                                display:
                                    true
                            }
                        }
                    }
                }
            });

        chatBody.scrollTop =
            chatBody.scrollHeight;
    }


    /*
     * Fungsi ini hanya mencari bubble
     * statistik dan menempelkan tombol Chart.
     *
     * Jangan menaruh removeOldChart()
     * atau setQuickChatVisibility() di sini.
     */
    function scanStatisticsMessages() {
        const chatBody =
            document.getElementById(
                "chatBody"
            );

        if (!chatBody) {
            return;
        }

        const messages =
            findStatisticsMessageElements(
                chatBody
            );

        messages.forEach(
            attachChartButton
        );
    }


    function startObserver() {
        const chatBody =
            document.getElementById(
                "chatBody"
            );

        if (!chatBody) {
            console.error(
                "statistics-chart.js: #chatBody belum ditemukan."
            );

            return;
        }

        scanStatisticsMessages();

        const observer =
            new MutationObserver(
                () => {
                    scanStatisticsMessages();
                }
            );

        observer.observe(
            chatBody,
            {
                childList: true,
                subtree: true,
                characterData: true
            }
        );
    }


    if (
        document.readyState ===
        "loading"
    ) {
        document.addEventListener(
            "DOMContentLoaded",
            startObserver
        );
    } else {
        startObserver();
    }
})();